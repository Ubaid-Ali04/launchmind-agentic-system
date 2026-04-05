import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
from message_bus import MessageBus
from agents.ceo import CEOAgent
from agents.product import ProductAgent
from agents.engineer import EngineerAgent
from agents.marketing import MarketingAgent
from agents.qa import QAAgent


bus = MessageBus()
bus.clear_messages()

ceo = CEOAgent(bus)
product = ProductAgent(bus)
engineer = EngineerAgent(bus)
marketing = MarketingAgent(bus)
qa = QAAgent(bus)

startup_idea = "FAST BookSwap: campus marketplace for used books"

print("\n--- CEO starting project ---")
ceo.start_project(startup_idea)

print("\n--- Product agent ---")
product.process_task()

print("\n--- Engineer agent ---")
engineer.process_task()

print("\n--- Marketing agent ---")
marketing.process_task()

print("\n--- QA agent ---")
qa.review_outputs()

print("\n--- CEO revision decision ---")
ceo.handle_qa_feedback()

print("\n--- Engineer revision ---")
engineer.handle_revision()

print("\n--- GitHub PR creation ---")
engineer.create_github_pr()
# Slack Notification
# ---------------------------
from slack_sdk import WebClient
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("SLACK_BOT_TOKEN")
channel = os.getenv("SLACK_CHANNEL")

try:
    client = WebClient(token=token)
    client.chat_postMessage(
        channel=channel,
        text="🚀 LaunchMind Multi-Agent workflow completed successfully!\nGitHub PR created."
    )
    print("Slack notification sent.")
except Exception as e:
    print("Slack error:", e)

print("\n--- Final Messages ---")
for msg in bus.get_messages():
    print(json.dumps(msg, indent=2, ensure_ascii=False))