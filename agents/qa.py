import os
from github import Github
from dotenv import load_dotenv
from message_bus import MessageBus

load_dotenv()


class QAAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "QA"

    def post_github_comments(self):
        token = os.getenv("GITHUB_TOKEN")
        repo_name = os.getenv("GITHUB_REPO")

        if not token or not repo_name:
            print("GitHub config missing for QA.")
            return None

        g = Github(token)
        repo = g.get_repo(repo_name)

        pulls = repo.get_pulls(state="open")
        if pulls.totalCount == 0:
            print("No open PR found for QA review.")
            return None

        pr = pulls[0]

        # comment 1
        pr.create_issue_comment(
            "QA Review: Consider adding stronger CTA button text."
        )

        # comment 2
        pr.create_issue_comment(
            "QA Review: Add contact email in landing page footer."
        )

        print("QA comments posted on GitHub PR.")

    def review_outputs(self):
        messages = self.bus.get_messages()

        engineering_output = None
        marketing_output = None

        for msg in messages:
            if msg["message_type"] == "result":
                if msg["payload"].get("result_type") == "engineering_output":
                    engineering_output = msg
                if msg["payload"].get("result_type") == "marketing_output":
                    marketing_output = msg

        feedback = []

        if engineering_output:
            feedback.append("Add stronger CTA button and contact email.")

        if marketing_output:
            feedback.append("Marketing message should include urgency.")

        feedback_text = " | ".join(feedback)

        # Post GitHub PR comments
        self.post_github_comments()

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="result",
            payload={
                "result_type": "qa_feedback",
                "feedback": feedback_text
            }
        )

        return response