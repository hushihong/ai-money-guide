# AI代写机器人部署指南

## 快速部署（5分钟）

### 第1步：创建Telegram机器人（2分钟）

1. 在Telegram中搜索 **@BotFather**
2. 发送 `/newbot`
3. 输入机器人名称：`AI代写服务`
4. 输入机器人用户名：`hsh_writer_bot`（或其他可用名称）
5. 复制获得的Token（格式：`1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`）

### 第2步：获取OpenAI API Key（可选）

如果要用ChatGPT生成内容：
1. 访问：https://platform.openai.com/api-keys
2. 创建API Key
3. 复制Key

### 第3步：配置机器人（1分钟）

创建 `.env` 文件：
```bash
cd /root/.openclaw/workspace/ai-writer-bot
cp .env.example .env
nano .env
```

填入：
```
BOT_TOKEN=你的机器人Token
OPENAI_API_KEY=你的OpenAI_Key
```

### 第4步：安装依赖（1分钟）

```bash
pip3 install -r requirements.txt
```

### 第5步：启动机器人（1分钟）

```bash
python3 bot.py
```

---

## 后台运行

使用screen后台运行：
```bash
screen -S ai-writer-bot
python3 bot.py
# 按 Ctrl+A+D 退出screen
```

或使用nohup：
```bash
nohup python3 bot.py > bot.log 2>&1 &
```

---

## 测试机器人

1. 在Telegram中搜索你的机器人用户名
2. 发送 `/start`
3. 测试下单流程

---

## 收款方式

机器人支持两种收款方式：

### 方式1：手动确认（当前）
- 用户扫码支付
- 用户点击"已支付"
- 你确认收款后生成内容

### 方式2：自动收款（需开通）
- 集成支付API
- 自动确认支付
- 需要支付接口

---

## 管理订单

查看订单：
```bash
cat orders.json
```

订单格式：
```json
{
  "ORD20260221123456": {
    "user_id": 123456789,
    "service": "resume",
    "requirement": "简历优化...",
    "content": "生成的内容...",
    "status": "completed",
    "created_at": "2026-02-21T12:34:56"
  }
}
```

---

## 机器人链接

创建完成后，用户访问：
```
https://t.me/hsh_writer_bot
```

---

## 费用

- Telegram机器人：免费
- OpenAI API：按使用量计费
  - GPT-3.5: $0.002/1K tokens
  - GPT-4: $0.03/1K tokens

---

## 下一步

1. 创建机器人（@BotFather）
2. 把Token发给我
3. 我帮你完成配置和启动

---

**准备好创建机器人了吗？**
