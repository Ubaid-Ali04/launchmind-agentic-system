import os
import requests
from dotenv import load_dotenv
from message_bus import MessageBus

load_dotenv()


class MarketingAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "Marketing"

    def send_email(self, subject, body):
        url = "https://api.sendgrid.com/v3/mail/send"

        headers = {
            "Authorization": f"Bearer {os.getenv('SENDGRID_API_KEY')}",
            "Content-Type": "application/json"
        }

        data = {
            "personalizations": [
                {
                    "to": [{"email": os.getenv("EMAIL_TO")}],
                    "subject": subject
                }
            ],
            "from": {"email": os.getenv("EMAIL_FROM")},
            "content": [
                {
                    "type": "text/html",
                    "value": f"<p>{body}</p>"
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 202:
            print("Email sent successfully.")
        else:
            print("Email error:", response.status_code, response.text)

    def process_task(self):
        messages = self.bus.get_messages_for_agent(self.name)
        if not messages:
            return None

        latest_task = messages[-1]
        startup_idea = latest_task["payload"].get("startup_idea", "Startup")

        marketing_content = {
            "tagline": "Swap books, save money.",
            "social_post": "FAST BookSwap is here! Exchange books with students.",
            "cold_email": "Join FAST BookSwap to access affordable study materials.",
            "slack_message": f"{startup_idea} launching soon!"
        }

        # Send real email
        self.send_email(
            subject="LaunchMind: FAST BookSwap Launch",
            body="FAST BookSwap is launching. Join early access today!"
        )

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="result",
            payload={
                "result_type": "marketing_output",
                "content": marketing_content
            },
            parent_message_id=latest_task["message_id"]
        )

        return response