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

startup_idea = "FAST BookSwap: a campus marketplace for used books, notes, and study materials."

print("\n--- CEO starting project ---")
ceo.start_project(startup_idea)

print("\n--- Product agent working ---")
product.process_task()

print("\n--- Engineer agent working ---")
engineer.process_task()

print("\n--- Marketing agent working ---")
marketing_response = marketing.process_task()

print("\nMarketing response:")
print(json.dumps(marketing_response, indent=2, ensure_ascii=False))

print("\nAll messages in bus:")
for msg in bus.get_messages():
    print(json.dumps(msg, indent=2, ensure_ascii=False))

print("\n--- QA agent reviewing ---")
qa_response = qa.review_outputs()

print("\nQA response:")
print(json.dumps(qa_response, indent=2, ensure_ascii=False))

print("\n--- CEO reviewing QA feedback ---")
revision = ceo.handle_qa_feedback()

print("\nCEO revision request:")
print(json.dumps(revision, indent=2, ensure_ascii=False))

print("\n--- Engineer applying revision ---")
rev = engineer.handle_revision()

print("\nRevision result:")
print(json.dumps(rev, indent=2, ensure_ascii=False))