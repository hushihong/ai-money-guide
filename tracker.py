#!/usr/bin/env python3
"""
推广追踪系统
记录推广活动、访问量、收益
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

# 配置
DATA_DIR = Path("/root/.openclaw/workspace/promotion-data")
DATA_DIR.mkdir(exist_ok=True)

# 数据文件
PROMOTION_LOG = DATA_DIR / "promotion_log.json"
STATS_FILE = DATA_DIR / "stats.json"

def init_data():
    """初始化数据文件"""
    if not PROMOTION_LOG.exists():
        with open(PROMOTION_LOG, 'w', encoding='utf-8') as f:
            json.dump({"logs": []}, f, ensure_ascii=False, indent=2)

    if not STATS_FILE.exists():
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            json.dump({
                "start_date": datetime.now().isoformat(),
                "total_promotions": 0,
                "daily_stats": {},
                "earnings": {
                    "buy_me_a_coffee": 0,
                    "github_sponsors": 0,
                    "total": 0
                }
            }, f, ensure_ascii=False, indent=2)

def log_promotion(platform, action, link=None):
    """记录推广活动"""
    with open(PROMOTION_LOG, 'r', encoding='utf-8') as f:
        data = json.load(f)

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "platform": platform,
        "action": action,
        "link": link
    }

    data["logs"].append(log_entry)

    with open(PROMOTION_LOG, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 更新统计
    update_stats()

def update_stats():
    """更新统计数据"""
    with open(PROMOTION_LOG, 'r', encoding='utf-8') as f:
        log_data = json.load(f)

    with open(STATS_FILE, 'r', encoding='utf-8') as f:
        stats = json.load(f)

    # 统计每日推广次数
    today = datetime.now().strftime("%Y-%m-%d")
    today_count = sum(1 for log in log_data["logs"]
                     if log["timestamp"].startswith(today))

    stats["total_promotions"] = len(log_data["logs"])
    stats["daily_stats"][today] = today_count

    with open(STATS_FILE, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

def add_earning(source, amount):
    """添加收益"""
    with open(STATS_FILE, 'r', encoding='utf-8') as f:
        stats = json.load(f)

    stats["earnings"][source] += amount
    stats["earnings"]["total"] = sum(stats["earnings"].values()) - stats["earnings"]["total"] + amount

    with open(STATS_FILE, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

def get_stats():
    """获取统计数据"""
    with open(STATS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def show_report():
    """显示报告"""
    stats = get_stats()
    today = datetime.now().strftime("%Y-%m-%d")

    print("\n" + "="*50)
    print("📊 推广统计报告")
    print("="*50)
    print(f"\n📅 开始时间: {stats['start_date'][:10]}")
    print(f"📈 总推广次数: {stats['total_promotions']}")
    print(f"📅 今日推广: {stats['daily_stats'].get(today, 0)} 次")

    print("\n💰 收益统计:")
    print(f"   Buy Me a Coffee: ${stats['earnings']['buy_me_a_coffee']}")
    print(f"   GitHub Sponsors: ${stats['earnings']['github_sponsors']}")
    print(f"   总计: ${stats['earnings']['total']}")

    print("\n🎯 目标进度:")
    print(f"   第一个月目标: $5-15")
    print(f"   当前进度: ${stats['earnings']['total']}")

    if stats['earnings']['total'] >= 5:
        print("   ✅ 已达到最低目标！")
    else:
        progress = (stats['earnings']['total'] / 5) * 100
        print(f"   进度: {progress:.1f}%")

    print("\n" + "="*50)

def main():
    """主函数"""
    init_data()

    print("🚀 推广追踪系统")
    print("="*50)

    while True:
        print("\n操作选项:")
        print("1. 记录推广活动")
        print("2. 添加收益")
        print("3. 查看报告")
        print("4. 退出")

        choice = input("\n选择 (1-4): ").strip()

        if choice == "1":
            print("\n平台选择:")
            print("1. Telegram")
            print("2. 朋友圈")
            print("3. 知乎")
            print("4. 微博")
            print("5. 其他")

            platform_choice = input("选择平台 (1-5): ").strip()
            platforms = {
                "1": "Telegram",
                "2": "朋友圈",
                "3": "知乎",
                "4": "微博",
                "5": "其他"
            }

            platform = platforms.get(platform_choice, "未知")
            action = input("推广动作 (如: 分享链接): ").strip()

            log_promotion(platform, action)
            print("✅ 已记录")

        elif choice == "2":
            print("\n收益来源:")
            print("1. Buy Me a Coffee")
            print("2. GitHub Sponsors")

            source_choice = input("选择来源 (1-2): ").strip()
            sources = {
                "1": "buy_me_a_coffee",
                "2": "github_sponsors"
            }

            source = sources.get(source_choice)
            if source:
                try:
                    amount = float(input("金额 (美元): ").strip())
                    add_earning(source, amount)
                    print("✅ 已记录")
                except ValueError:
                    print("❌ 金额格式错误")

        elif choice == "3":
            show_report()

        elif choice == "4":
            print("👋 再见！")
            break

        else:
            print("❌ 无效选择")

if __name__ == "__main__":
    main()
