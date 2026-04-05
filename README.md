# 🚀 LaunchMind — Multi-Agent Startup Builder

LaunchMind is an **Agentic AI system** that autonomously plans, builds, reviews, and improves a startup idea using coordinated AI agents.

The system demonstrates **multi-agent orchestration**, **LLM-based decision making**, **QA feedback loops**, and **automated GitHub workflow integration**.

---

## 🧠 System Overview

LaunchMind simulates a startup team where specialized AI agents collaborate:

* 👨‍💼 **CEO Agent** — Task planning & decision making (LLM-powered)
* 📦 **Product Agent** — Product specification generation
* 🛠 **Engineer Agent** — Landing page creation & revisions
* 📢 **Marketing Agent** — Marketing content + Email + Slack
* 🧪 **QA Agent** — Quality review & feedback loop
* 📨 **Message Bus** — Structured inter-agent communication

---

## 🏗 Architecture Diagram

```
                +----------------+
                |    CEO Agent   |
                +--------+-------+
                         |
    -------------------------------------------
    |                     |                  |
+------------+   +--------------+   +------------+
| Product    |   |  Engineer    |   | Marketing  |
|   Agent    |   |    Agent     |   |   Agent    |
+------------+   +--------------+   +------------+
       |                |                  |
 Product Spec      Landing Page      Email + Slack
                         |
                     GitHub Issue
                         |
                     GitHub PR
                         |
                     +--------+
                     |  QA    |
                     | Agent  |
                     +---+----+
                         |
                    Feedback Loop
                         |
                     CEO Decision
                         |
                 Engineer Revision
```

---

## 🔄 Message Flow

```
CEO → Product → CEO
CEO → Engineer → CEO
CEO → Marketing → CEO
QA → CEO → Engineer (revision)
Engineer → GitHub (Issue + PR)
Marketing → Email + Slack
```

---

## ✨ Features

* Multi-agent autonomous collaboration
* Structured message-based communication
* LLM-powered CEO reasoning
* QA feedback and revision loop
* GitHub Issue auto-creation
* GitHub Pull Request automation
* Landing page generation
* Slack notification integration
* SendGrid email integration
* Fallback logic when LLM unavailable
* End-to-end autonomous startup pipeline

---

## 📂 Project Structure

```
launchmind-agentic-system/
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
├── landing_page.html
├── messages.json
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Setup

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/launchmind-agentic-system.git
cd launchmind-agentic-system
```

### 2. Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
GITHUB_TOKEN=your_token_here
GITHUB_REPO=username/repo
SLACK_WEBHOOK_URL=your_webhook
SENDGRID_API_KEY=your_sendgrid_key
EMAIL_FROM=verified_email
EMAIL_TO=receiver_email
```

---

## ▶️ Run System

```
python main.py
```

---

## 🔄 Workflow

1. CEO analyzes startup idea
2. Tasks distributed to Product, Engineer, Marketing
3. Agents generate outputs
4. QA reviews outputs
5. CEO decides revision
6. Engineer updates landing page
7. GitHub Issue automatically created
8. GitHub Pull Request created
9. Slack notification sent
10. Email notification sent

---

## 🧪 Example Output

* Product specification generated
* Landing page created
* Marketing content produced
* QA feedback applied
* GitHub Issue created
* GitHub Pull Request created
* Slack notification sent
* Email notification delivered

---

## 🤖 LLM Integration

CEO agent uses LLM for:

* Task decomposition
* Revision decision making
* Agent coordination

Fallback logic ensures the system runs even when API quota is unavailable.

---

## 📈 Learning Objectives

* Agentic AI system design
* Multi-agent orchestration
* Structured message schema
* LLM integration
* GitHub automation
* QA feedback loops
* Autonomous workflow pipelines

---

## 👨‍💻 Author

**Ubaid Ali**
MS Data Science — FAST NUCES

---

## 📜 License

This project is for academic and research purposes.

---

## ⭐ Acknowledgment

Built as part of an Agentic AI assignment demonstrating autonomous multi-agent collaboration and workflow automation.
