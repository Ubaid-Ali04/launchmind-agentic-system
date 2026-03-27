# LaunchMind Agentic System

## Overview

LaunchMind is a multi-agent startup simulation system where autonomous AI agents collaborate to design, build, and launch a startup idea. The system demonstrates agent-to-agent communication, feedback loops, and automated GitHub pull request creation.

## Agents

* **CEO Agent** – Decomposes startup idea into tasks
* **Product Agent** – Creates product specification
* **Engineer Agent** – Builds landing page and handles revisions
* **Marketing Agent** – Generates marketing content
* **QA Agent** – Reviews outputs and provides feedback

## Architecture

Agents communicate through a centralized Message Bus.
Workflow:
CEO → Product → Engineer → Marketing → QA → CEO → Engineer (revision) → GitHub PR

## Features

* Multi-agent collaboration
* Message bus communication
* QA feedback loop
* Automatic revision handling
* GitHub Pull Request automation
* End-to-end agentic workflow

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

## Example Workflow

1. CEO assigns tasks
2. Product defines requirements
3. Engineer builds landing page
4. Marketing generates content
5. QA reviews outputs
6. CEO requests revision
7. Engineer updates code
8. Engineer creates GitHub Pull Request automatically

## GitHub Automation

Engineer agent:

* Creates new branch
* Updates landing page
* Opens Pull Request
* Supports merge workflow

## Output Example

* Landing page generated
* Marketing content created
* QA feedback issued
* GitHub PR automatically created

## Tech Stack

* Python
* Multi-agent architecture
* GitHub API (PyGithub)
* dotenv
* Message Bus Pattern

## Author

Ubaid Ali – FAST NUCES MS Data Science
