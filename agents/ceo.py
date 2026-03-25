from message_bus import MessageBus
from typing import Optional, Dict


class CEOAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "CEO"

    def start_project(self, startup_idea: str):
        product_task = {
            "task": "Create product specification",
            "startup_idea": startup_idea,
            "requirements": [
                "Define target users",
                "Define core features",
                "Define value proposition",
                "Define simple user flow"
            ]
        }

        engineer_task = {
            "task": "Build landing page",
            "startup_idea": startup_idea,
            "requirements": [
                "Create a clean HTML landing page",
                "Include title, subtitle, features, and CTA button",
                "Prepare code for GitHub commit and PR"
            ]
        }

        marketing_task = {
            "task": "Create marketing content",
            "startup_idea": startup_idea,
            "requirements": [
                "Write tagline",
                "Write short social post",
                "Write cold email",
                "Prepare Slack announcement"
            ]
        }

        m1 = self.bus.create_message(
            from_agent=self.name,
            to_agent="Product",
            message_type="task_assignment",
            payload=product_task
        )

        m2 = self.bus.create_message(
            from_agent=self.name,
            to_agent="Engineer",
            message_type="task_assignment",
            payload=engineer_task
        )

        m3 = self.bus.create_message(
            from_agent=self.name,
            to_agent="Marketing",
            message_type="task_assignment",
            payload=marketing_task
        )

        return [m1, m2, m3]

    def review_feedback(self, feedback_text: str, parent_message_id: str = None):
        needs_revision = any(
            keyword in feedback_text.lower()
            for keyword in ["improve", "revise", "missing", "weak", "fix", "add", "issue"]
        )

        response = {
            "feedback_received": feedback_text,
            "decision": "revision_required" if needs_revision else "approved",
            "next_action": "Ask agent to revise output" if needs_revision else "Proceed to finalization"
        }

        return self.bus.create_message(
            from_agent=self.name,
            to_agent="QA" if needs_revision else "System",
            message_type="review_result",
            payload=response,
            parent_message_id=parent_message_id
        )

    def handle_qa_feedback(self) -> Optional[Dict]:
        messages = self.bus.get_messages()

        qa_feedback = None
        for msg in reversed(messages):
            if msg["message_type"] == "qa_feedback":
                qa_feedback = msg
                break

        if not qa_feedback:
            return None

        feedback_text = qa_feedback["payload"]["feedback"]

        revision_task = {
            "task": "Revise landing page based on QA feedback",
            "feedback": feedback_text
        }

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="Engineer",
            message_type="revision_request",
            payload=revision_task,
            parent_message_id=qa_feedback["message_id"]
        )

        return response