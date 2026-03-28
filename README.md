# 🚀 LaunchMind — Multi-Agent Startup Builder

An Agentic AI system that autonomously plans, builds, reviews, and improves a startup idea using coordinated AI agents.

This project demonstrates a **multi-agent architecture**, **LLM-driven decision making**, **QA feedback loops**, and **automated GitHub pull request generation**.

---

# 🧠 System Overview

LaunchMind simulates a startup team where specialized AI agents collaborate:

* 👨‍💼 CEO Agent — Task planning & decision making (LLM powered)
* 📦 Product Agent — Product specification generation
* 🛠 Engineer Agent — Landing page creation & revisions
* 📢 Marketing Agent — Marketing content generation
* 🧪 QA Agent — Quality review & feedback
* 📨 Message Bus — Structured inter-agent communication

---

# 🏗 Architecture

CEO → Product
CEO → Engineer
CEO → Marketing
Agents → QA
QA → CEO
CEO → Engineer (revision)
Engineer → GitHub PR

---

# ✨ Features

* Multi-agent coordination
* Structured message schema
* LLM-based CEO reasoning
* QA feedback loop
* Automated revision workflow
* GitHub branch + PR automation
* Fallback logic for LLM quota handling
* End-to-end autonomous pipeline

---

# 📂 Project Structure

```
launchmind-agents/
│
├── agents/
│   ├── ceo.py
│   ├── product.py
│   ├── engineer.py
│   ├── marketing.py
│   └── qa.py
│
├── message_bus.py
├── main.py
├── config.py
├── requirements.txt
├── .env.example
└── landing_page.html
```

---

# ⚙️ Setup

### 1. Clone repository

```
git clone https://github.com/YOUR_USERNAME/launchmind-agentic-system.git
cd launchmind-agentic-system
```

### 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env`

```
OPENAI_API_KEY=your_key_here
GITHUB_TOKEN=your_token_here
GITHUB_REPO=username/repo
GITHUB_BRANCH=main
```

---

# ▶️ Run System

```
python main.py
```

---

# 🔄 Workflow

1. CEO analyzes startup idea
2. Tasks distributed to agents
3. Agents generate outputs
4. QA reviews outputs
5. CEO decides revision
6. Engineer updates landing page
7. GitHub PR automatically created

---

# 🧪 Example Output

* Product specification generated
* Landing page created
* Marketing content produced
* QA feedback applied
* GitHub Pull Request created automatically

---

# 🤖 LLM Integration

CEO agent uses LLM for:

* Task decomposition
* QA decision making

Fallback logic ensures system runs without API quota.

---

# 📈 Learning Objectives

* Agentic AI system design
* Multi-agent communication
* Structured message schema
* LLM integration
* GitHub automation
* Autonomous workflows

---

# 👨‍💻 Author

**Ubaid Ali**
MS Data Science — FAST NUCES

---

# 📜 License

This project is for academic and research purposes.

---

# ⭐ Acknowledgment

Built as part of Agentic AI assignment demonstrating autonomous multi-agent collaboration.
