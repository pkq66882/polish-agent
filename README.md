# Polish Agent ✨

自动邮件 / 消息润色工具

## 功能
- 三种语气输出（正式 / 中性 / 友好）
- CLI + API + Web
- 支持中英文

## 启动

### 1. 安装依赖
pip install -r requirements.txt

### 2. 配置环境变量
cp .env.example .env

### 3. 启动API
uvicorn app.main:app --reload

访问：
http://127.0.0.1:8000/docs

### 4. CLI
python cli.py
