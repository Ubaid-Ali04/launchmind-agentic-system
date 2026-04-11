# 🚀 LaunchMind — Multi-Agent Startup Builder

LaunchMind is an **Agentic AI system** that autonomously plans, builds, reviews, and improves a startup idea using coordinated AI agents.

The system demonstrates **multi-agent orchestration**, **LLM-based decision making**, **QA feedback loops**, and **automated GitHub workflow integration**.

---

## 💡 Startup Idea

FAST BookSwap is a campus-based marketplace that allows students to buy, sell, and trade used textbooks within their university.
Students verify using university email, list books using ISBN scanning, and coordinate safe on-campus meetups.
The goal is to reduce textbook costs and promote sustainable reuse of academic materials.

---

## 🧠 System Overview

LaunchMind simulates a startup team where specialized AI agents collaborate:

* 👨‍💼 **CEO Agent** — Task planning & decision making (LLM-powered)
* 📦 **Product Agent** — Product specification generation
* 🛠 **Engineer Agent** — Landing page creation & revisions + GitHub automation
* 📢 **Marketing Agent** — Marketing content + Email + Slack Block Kit message
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
Engineer → GitHub (Issue + PR)
Marketing → Email + Slack
QA → CEO → Engineer (revision)
CEO → Slack Final Summary
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
* Slack Block Kit notification
* SendGrid email integration
* End-to-end autonomous startup pipeline
* Real-world platform automation

---

## 🔗 Platform Integrations

| Platform         | Agent           | Action                                        |
| ---------------- | --------------- | --------------------------------------------- |
| GitHub           | Engineer Agent  | Creates issue, commits landing page, opens PR |
| GitHub           | QA Agent        | Posts inline review comments                  |
| Slack            | Marketing Agent | Posts launch message using Block Kit          |
| Slack            | CEO Agent       | Posts final summary                           |
| Email (SendGrid) | Marketing Agent | Sends cold outreach email                     |

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
git clone https://github.com/Ubaid-Ali04/launchmind-agentic-system.git
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
GEMINI_API_KEY=your_key_here
GITHUB_TOKEN=your_token_here
GITHUB_REPO=username/repo
SLACK_BOT_TOKEN=your_token
SLACK_CHANNEL=#launches
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
3. Product generates product specification
4. Engineer builds landing page
5. Marketing generates copy and sends email
6. Engineer creates GitHub Issue and Pull Request
7. Marketing posts Slack launch message
8. QA reviews PR and posts comments
9. CEO reasons over QA feedback
10. Engineer revises landing page
11. CEO posts final Slack summary

---

## 🔗 Example GitHub Pull Request

https://github.com/Ubaid-Ali04/launchmind-agentic-system/pull/2

---

## 💬 Slack Integration

The Marketing agent posts a Block Kit launch message, and the CEO agent posts the final summary message after QA review and revision.

(Slack screenshots should be added here for submission)

---

## 🧪 Example Outputs

* Product specification generated
* Landing page created
* Marketing content produced
* QA feedback applied
* GitHub Issue created
* GitHub Pull Request created
* Slack launch message posted
* Email notification delivered
* CEO final summary posted

---

## 🎓 Learning Objectives

* Agentic AI system design
* Multi-agent orchestration
* Structured message schema
* LLM integration
* GitHub automation
* QA feedback loops
* Autonomous workflow pipelines

---
## 👥 Group Members

| Name 
|------------
| Ubaid Ali 
| Muhammad Saad 
| Tasawar Hasnain 

## 📜 License

This project is for academic and research purposes.

---

## ⭐ Acknowledgment

Built as part of an Agentic AI assignment demonstrating autonomous multi-agent collaboration and workflow automation.

## 📸 Demo Screenshots

### Marketing Slack Message
![Marketing Slack](screenshots/slack_marketing.png)

### CEO Final Summary
![CEO Summary](screenshots/slack_ceo_summary.png)

### GitHub Pull Request
![GitHub PR](screenshots/github_pr.png)