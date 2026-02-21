# 📖 使用指南

## 快速开始

### 方式一：一键部署（推荐）

```bash
# 1. 运行一键部署脚本
./auto-deploy.sh

# 2. 按照提示完成GitHub Pages配置

# 3. 添加赞助链接
./add-sponsor-links.sh
git commit -am "Add sponsor links"
git push
```

### 方式二：手动部署

```bash
# 1. 创建GitHub仓库
# 访问 https://github.com/new
# 仓库名：ai-money-guide
# 设置为Public

# 2. 推送代码
git init
git add .
git commit -m "Add AI赚钱项目教程"
git remote add origin <你的仓库URL>
git branch -M main
git push -u origin main

# 3. 启用GitHub Pages
# 进入仓库 Settings → Pages
# Source选择：Deploy from a branch
# Branch选择：main，文件夹：/ (root)
# 保存

# 4. 添加赞助链接
./add-sponsor-links.sh
git commit -am "Add sponsor links"
git push
```

## 文件说明

```
.
├── index.html              # 主页面（包含所有项目）
├── README.md               # 项目说明
├── USAGE.md                # 使用指南
├── auto-deploy.sh          # 一键部署脚本
├── deploy.sh               # 部署脚本
├── add-sponsor-links.sh    # 添加赞助链接脚本
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Pages部署配置
```

## 修改内容

### 修改项目详情

编辑 `index.html`：
- 修改项目名称、收益、步骤
- 调整样式（修改CSS部分）

### 添加赞助链接

```bash
./add-sponsor-links.sh
```

输入你的GitHub用户名，脚本会自动替换所有链接。

### 自定义域名

1. 在GitHub仓库设置中添加自定义域名
2. 在域名DNS设置中添加CNAME记录
3. 重新部署

## 监控收益

### GitHub Sponsors

- 访问 https://github.com/sponsors
- 查看赞助列表和金额
- 可设置每月赞助目标

### Buy Me a Coffee

- 访问 https://www.buymeacoffee.com
- 查看订阅列表和收入
- 可设置每月目标

## 推广策略

### 社交媒体

1. **Twitter/X**
   - 分享项目链接
   - 使用相关标签：#AI赚钱 #副业 #被动收入

2. **Telegram**
   - 加入赚钱相关的群组
   - 分享项目链接

3. **知乎/B站**
   - 写相关文章/视频
   - 在简介中添加链接

### 内容营销

1. **创建教程**
   - 详细介绍每个项目
   - 分享成功案例

2. **案例研究**
   - 记录实际执行过程
   - 分享收入数据

3. **答疑解惑**
   - 回答读者问题
   - 提供帮助

## 避坑指南

### ❌ 常见错误

1. **忘记配置GitHub Pages**
   - 导致页面无法访问

2. **赞助链接未替换**
   - 显示错误的用户名

3. **仓库设置为Private**
   - 无法通过GitHub访问

4. **未推送代码**
   - 页面不更新

### ✅ 最佳实践

1. **定期更新**
   - 每月更新项目信息
   - 添加新项目

2. **收集反馈**
   - 询问用户需求
   - 改进内容

3. **保持透明**
   - 分享真实数据
   - 诚实记录

## 收益统计

### 目标

- **第一个月**：5-10美元
- **第二个月**：10-20美元
- **第三个月**：20-50美元
- **第六个月**：50-100美元

### 方法

1. **直接赞助**
   - GitHub Sponsors
   - Buy Me a Coffee

2. **项目执行**
   - 网盘推广
   - 小说推文
   - 短剧推广

## 支持

如有问题，请：
1. 查看本文档
2. 访问项目仓库Issues
3. 联系作者

## 更新日志

- **2026-02-21**：初始版本
  - 创建5个项目教程
  - 添加部署脚本
  - 完善使用文档
