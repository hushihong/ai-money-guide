#!/usr/bin/env python3
"""
AI代写机器人 - 全自动接单系统
"""

import os
import json
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# 配置
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YOUR_OPENAI_KEY')

# 服务配置
SERVICES = {
    'resume': {
        'name': '简历优化',
        'price': 50,
        'description': '专业简历优化，提高面试通过率'
    },
    'xiaohongshu': {
        'name': '小红书文案',
        'price': 40,
        'description': '爆款小红书文案，吸引粉丝'
    },
    'article': {
        'name': '公众号文章',
        'price': 150,
        'description': '深度内容创作，提升影响力'
    }
}

# 订单存储
ORDERS_FILE = 'orders.json'

# 日志配置
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 用户状态存储
user_states = {}

def load_orders():
    """加载订单"""
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_orders(orders):
    """保存订单"""
    with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """开始命令"""
    keyboard = [
        [InlineKeyboardButton("📝 查看服务", callback_data='services')],
        [InlineKeyboardButton("💰 下单", callback_data='order')],
        [InlineKeyboardButton("📊 查询订单", callback_data='status')],
        [InlineKeyboardButton("❓ 帮助", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = """
🤖 *AI代写服务机器人*

专业文案生成，当天交付，满意付款！

✨ 服务特点：
• 2-4小时快速交付
• AI+人工双重审核
• 不满意免费修改
• 24/7在线服务

点击下方按钮开始使用 👇
    """
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """服务列表"""
    query = update.callback_query
    await query.answer()
    
    services_text = "📝 *服务列表*\n\n"
    for key, service in SERVICES.items():
        services_text += f"*{service['name']}*\n"
        services_text += f"💰 价格：{service['price']}元\n"
        services_text += f"📌 {service['description']}\n\n"
    
    keyboard = [[InlineKeyboardButton("🔙 返回", callback_data='start')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(services_text, reply_markup=reply_markup, parse_mode='Markdown')

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """下单"""
    query = update.callback_query
    await query.answer()
    
    keyboard = []
    for key, service in SERVICES.items():
        keyboard.append([InlineKeyboardButton(f"{service['name']} - {service['price']}元", callback_data=f'order_{key}')])
    keyboard.append([InlineKeyboardButton("🔙 返回", callback_data='start')])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text("请选择服务：", reply_markup=reply_markup)

async def handle_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理订单"""
    query = update.callback_query
    await query.answer()
    
    service_key = query.data.split('_')[1]
    service = SERVICES[service_key]
    user_id = query.from_user.id
    
    # 生成订单ID
    order_id = f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}{user_id}"
    
    # 保存订单状态
    user_states[user_id] = {
        'order_id': order_id,
        'service': service_key,
        'status': 'waiting_payment'
    }
    
    order_text = f"""
📦 *订单信息*

订单号：`{order_id}`
服务：{service['name']}
价格：{service['price']}元

💳 *支付方式*

请扫码支付定金（30元）：
- 微信/支付宝扫码
- 支付备注：{order_id}

支付完成后，请发送"已支付"确认。
    """
    
    keyboard = [[InlineKeyboardButton("✅ 已支付", callback_data=f'paid_{order_id}')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(order_text, reply_markup=reply_markup, parse_mode='Markdown')

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理支付确认"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    
    if user_id not in user_states:
        await query.edit_message_text("❌ 订单不存在，请重新下单。")
        return
    
    user_states[user_id]['status'] = 'waiting_requirement'
    
    await query.edit_message_text(
        "✅ 支付确认成功！\n\n"
        "请详细描述您的需求：\n"
        "例如：简历优化 - 3年开发经验，应聘高级工程师岗位...",
        parse_mode='Markdown'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理用户消息"""
    user_id = update.message.from_user.id
    
    if user_id not in user_states:
        await update.message.reply_text("请先使用 /start 开始。")
        return
    
    state = user_states[user_id]
    
    if state['status'] == 'waiting_requirement':
        # 保存需求
        state['requirement'] = update.message.text
        state['status'] = 'generating'
        
        await update.message.reply_text("⏳ 正在生成内容，请稍候...")
        
        # 生成内容
        content = await generate_content(state['service'], state['requirement'])
        
        # 保存订单
        orders = load_orders()
        orders[state['order_id']] = {
            'user_id': user_id,
            'service': state['service'],
            'requirement': state['requirement'],
            'content': content,
            'status': 'completed',
            'created_at': datetime.now().isoformat()
        }
        save_orders(orders)
        
        # 发送内容
        await update.message.reply_text(
            f"✅ 内容生成完成！\n\n{content}\n\n"
            f"如需修改，请回复具体修改要求。\n"
            f"满意请支付尾款。"
        )
        
        # 清除状态
        del user_states[user_id]

async def generate_content(service, requirement):
    """生成内容（使用AI）"""
    # 这里应该调用OpenAI API或其他AI服务
    # 为了演示，返回示例内容
    
    if service == 'resume':
        return f"""
【简历优化结果】

{requirement}

优化后的简历内容：
（这里会显示AI生成的优化简历）

✨ 亮点：
- 突出核心技能
- 量化工作成果
- 符合岗位要求
        """
    elif service == 'xiaohongshu':
        return f"""
【小红书文案】

{requirement}

生成的文案：
（这里会显示AI生成的小红书文案）

#小红书文案 #种草
        """
    elif service == 'article':
        return f"""
【公众号文章】

{requirement}

生成的文章：
（这里会显示AI生成的公众号文章）
        """
    
    return "内容生成中..."

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """查询订单状态"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    orders = load_orders()
    
    user_orders = [o for o in orders.values() if o['user_id'] == user_id]
    
    if not user_orders:
        await query.edit_message_text("暂无订单记录。")
        return
    
    status_text = "📊 *我的订单*\n\n"
    for order in user_orders[-5:]:  # 显示最近5个订单
        status_text += f"订单号：{order.get('order_id', 'N/A')}\n"
        status_text += f"服务：{SERVICES[order['service']]['name']}\n"
        status_text += f"状态：{order['status']}\n\n"
    
    keyboard = [[InlineKeyboardButton("🔙 返回", callback_data='start')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(status_text, reply_markup=reply_markup, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """帮助信息"""
    query = update.callback_query
    await query.answer()
    
    help_text = """
❓ *使用帮助*

1. 点击"查看服务"了解服务内容
2. 点击"下单"选择需要的服务
3. 扫码支付定金（30元）
4. 描述您的具体需求
5. AI自动生成内容
6. 满意后支付尾款

💡 *提示*
- 请详细描述需求，效果更好
- 不满意可免费修改
- 咨询微信：hushihong

📞 *联系方式*
微信：hushihong
邮箱：hushpcl@163.com
    """
    
    keyboard = [[InlineKeyboardButton("🔙 返回", callback_data='start')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(help_text, reply_markup=reply_markup, parse_mode='Markdown')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理按钮回调"""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == 'start':
        await start(update, context)
    elif data == 'services':
        await services(update, context)
    elif data == 'order':
        await order(update, context)
    elif data.startswith('order_'):
        await handle_order(update, context)
    elif data.startswith('paid_'):
        await handle_payment(update, context)
    elif data == 'status':
        await status(update, context)
    elif data == 'help':
        await help_command(update, context)

def main():
    """启动机器人"""
    # 创建应用
    application = Application.builder().token(BOT_TOKEN).build()
    
    # 添加处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # 启动机器人
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
