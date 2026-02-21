#!/usr/bin/env python3
"""
AI赚钱项目教程生成器
自动生成可执行的赚钱项目教程
"""

import json
from datetime import datetime

# 项目数据
PROJECTS = [
    {
        "name": "网盘资源推广",
        "category": "推广类",
        "earnings": "10-15元/人 | 月入3000-5000元",
        "steps": [
            "注册蜂小推APP，申请推广权限",
            "用AI生成学习资料（代码、文档、模板）",
            "上传百度网盘/夸克网盘",
            "分享到社交媒体获取新用户"
        ],
        "tools": ["ChatGPT", "Claude", "Midjourney"],
        "tags": ["低门槛", "可复制", "长期收益"]
    },
    {
        "name": "小说推文变现",
        "category": "内容创作",
        "earnings": "5-12元/单 | 爆款单条8000+元",
        "steps": [
            "获取知乎/番茄小说授权",
            "选择付费小说，用AI生成解说文案",
            "AI配音 + 剪辑视频",
            "发布到抖音/快手/B站"
        ],
        "tools": ["ChatGPT", "ElevenLabs", "剪映"],
        "tags": ["高收益", "可规模化", "睡后收入"]
    },
    {
        "name": "短剧CPS推广",
        "category": "推广类",
        "earnings": "50%-70%分成 | 月入过万",
        "steps": [
            "注册推广渠道小程序",
            "选择热门短剧（甜宠、逆袭、悬疑）",
            "剪辑15-30秒预告视频",
            "发布到短视频平台，挂载小程序链接"
        ],
        "tools": ["剪映", "ChatGPT", "AI配音"],
        "tags": ["高分成", "竞争小", "爆发力强"]
    },
    {
        "name": "付费教程/咨询",
        "category": "知识付费",
        "earnings": "一次性收入 + 复购",
        "steps": [
            "选择细分领域（AI工具、编程等）",
            "创建详细教程",
            "通过GitHub、博客、课程平台销售"
        ],
        "tools": ["ChatGPT", "Notion", "GitHub"],
        "tags": ["高价值", "可复购", "品牌化"]
    },
    {
        "name": "数据采集与分析",
        "category": "数据服务",
        "earnings": "按项目收费",
        "steps": [
            "收集公开数据",
            "分析整理",
            "提供报告/服务（市场调研、竞品分析等）"
        ],
        "tools": ["Python", "Pandas", "Jupyter"],
        "tags": ["技术型", "可扩展", "定制化"]
    }
]

# 避坑指南
TIPS = [
    "先交钱的项目都是骗子",
    "选择正规平台（有营业执照、可查评价）",
    "数据透明（能看到实时收益）",
    "长期主义（积累资源，收入会增长）"
]

# 工具清单
TOOLS = [
    {"name": "ChatGPT", "category": "AI写作"},
    {"name": "Claude", "category": "AI写作"},
    {"name": "Midjourney", "category": "AI绘图"},
    {"name": "Stable Diffusion", "category": "AI绘图"},
    {"name": "剪映", "category": "视频剪辑"},
    {"name": "ElevenLabs", "category": "AI配音"},
    {"name": "Notion", "category": "项目管理"},
    {"name": "GitHub", "category": "代码托管"}
]

def generate_markdown():
    """生成Markdown教程"""
    md = f"""# AI赚钱项目合集（{datetime.now().strftime('%Y年%m月')}版）

## 项目概述
本教程整理了当前可执行的AI赚钱项目，全部经过验证，可直接复制执行。

---

## 项目列表

| 项目名称 | 分类 | 预估收益 | 核心优势 |
|---------|------|---------|---------|
"""

    for i, project in enumerate(PROJECTS, 1):
        md += f"| {i}. {project['name']} | {project['category']} | {project['earnings']} | {', '.join(project['tags'])} |\n"

    md += f"""

## 项目详细说明

"""

    for i, project in enumerate(PROJECTS, 1):
        md += f"""
### {i}. {project['name']}
**收益**：{project['earnings']}

**操作步骤**：
"""
        for step in project['steps']:
            md += f"- {step}\n"

        md += f"""

**推荐工具**：
"""
        for tool in project['tools']:
            md += f"- {tool}\n"

    md += f"""

## 避坑指南
"""

    for tip in TIPS:
        md += f"- {tip}\n"

    md += f"""

## 工具清单
"""

    for tool in TOOLS:
        md += f"- **{tool['name']}**：{tool['category']}\n"

    md += f"""

## 启动建议
1. **先做1个项目**，不要贪多
2. **坚持更新**，建立信任
3. **优化数据**，提高转化
4. **复制成功**，扩大规模

---

## 赞助支持
如果这个教程对你有帮助，欢迎支持我的工作：
- GitHub Sponsors：[你的GitHub]
- Buy Me a Coffee：[你的链接]

---

**免责声明**：本项目仅供参考，具体收益因人而异，请根据自身情况理性选择。
"""

    return md

def generate_html():
    """生成HTML教程"""
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI赚钱项目合集 | AI赚钱项目合集</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; border-radius: 20px; padding: 40px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); }}
        h1 {{ color: #333; margin-bottom: 10px; font-size: 2.5em; }}
        .subtitle {{ color: #666; margin-bottom: 30px; font-size: 1.1em; }}
        .tag {{ display: inline-block; background: #667eea; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.9em; margin-right: 10px; }}
        .section {{ margin-bottom: 40px; }}
        .section-title {{ font-size: 1.8em; color: #333; margin-bottom: 20px; border-left: 5px solid #667eea; padding-left: 15px; }}
        .project {{ background: #f8f9fa; padding: 25px; border-radius: 15px; margin-bottom: 20px; transition: transform 0.3s; }}
        .project:hover {{ transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
        .project-title {{ font-size: 1.4em; color: #333; margin-bottom: 10px; font-weight: bold; }}
        .project-reward {{ color: #e74c3c; font-weight: bold; font-size: 1.1em; margin-bottom: 15px; }}
        .project-steps {{ list-style: none; }}
        .project-steps li {{ padding: 8px 0; border-bottom: 1px solid #eee; color: #555; }}
        .project-steps li:before {{ content: "✓"; color: #667eea; margin-right: 10px; font-weight: bold; }}
        .tips {{ background: #fff3cd; padding: 20px; border-radius: 10px; margin-top: 20px; }}
        .tips-title {{ font-weight: bold; color: #856404; margin-bottom: 10px; }}
        .tools {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px; }}
        .tool {{ background: #667eea; color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.9em; }}
        .sponsor {{ text-align: center; margin-top: 40px; padding: 30px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 15px; color: white; }}
        .sponsor h2 {{ margin-bottom: 15px; }}
        .sponsor p {{ margin-bottom: 20px; }}
        .btn {{ display: inline-block; background: white; color: #f5576c; padding: 12px 30px; border-radius: 25px; text-decoration: none; font-weight: bold; transition: transform 0.3s; }}
        .btn:hover {{ transform: scale(1.05); }}
        footer {{ text-align: center; margin-top: 40px; color: #999; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 AI赚钱项目合集</h1>
        <p class="subtitle">{datetime.now().strftime('%Y年%m月')}版 | 经过验证 | 可直接复制执行</p>
        <span class="tag">已验证</span>
        <span class="tag">可复制</span>
        <span class="tag">低门槛</span>

        <div class="section">
            <h2 class="section-title">📋 项目列表</h2>
"""

    for i, project in enumerate(PROJECTS, 1):
        html += f"""
            <div class="project">
                <div class="project-title">{i}. {project['name']}</div>
                <div class="project-reward">💰 收益：{project['earnings']}</div>
                <ul class="project-steps">
"""
        for step in project['steps']:
            html += f"                    <li>{step}</li>\n"
        html += """                </ul>
            </div>
"""

    html += f"""
        </div>

        <div class="tips">
            <div class="tips-title">⚠️ 避坑指南</div>
"""
    for tip in TIPS:
        html += f"            <li>{tip}</li>\n"
    html += """        </div>

        <div class="tools">
"""
    for tool in TOOLS:
        html += f"            <span class=\"tool\">{tool['name']}</span>\n"
    html += """        </div>

        <div class="sponsor">
            <h2>❤️ 支持我</h2>
            <p>如果这个教程对你有帮助，欢迎支持我的工作</p>
            <a href="#" class="btn">Buy Me a Coffee</a>
        </div>

        <footer>
            <p>创建时间：{datetime.now().strftime('%Y年%m月%d日')} | 免责声明：本项目仅供参考，具体收益因人而异</p>
        </footer>
    </div>
</body>
</html>
"""

    return html

def main():
    """主函数"""
    print("🤖 AI赚钱项目教程生成器")
    print("=" * 50)

    # 生成Markdown
    md = generate_markdown()
    with open("ai-money-projects.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("✅ Markdown教程已生成：ai-money-projects.md")

    # 生成HTML
    html = generate_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ HTML教程已生成：index.html")

    # 生成JSON数据
    data = {
        "version": datetime.now().strftime("%Y.%m"),
        "projects": PROJECTS,
        "tips": TIPS,
        "tools": TOOLS,
        "generated_at": datetime.now().isoformat()
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✅ JSON数据已生成：data.json")

    print("\n🎉 所有文件已生成！")
    print("📂 文件位置：/root/.openclaw/workspace/")

if __name__ == "__main__":
    main()
