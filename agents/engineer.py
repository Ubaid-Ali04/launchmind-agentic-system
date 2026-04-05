import os
from github import Github
from dotenv import load_dotenv
from message_bus import MessageBus
from pathlib import Path


class EngineerAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "Engineer"

    def process_task(self):
        messages = self.bus.get_messages_for_agent(self.name)
        if not messages:
            return None

        latest_task = messages[-1]
        startup_idea = latest_task["payload"].get("startup_idea", "FAST BookSwap")

        html_content = f"""<!DOCTYPE html>
<html>
<head>
<title>{startup_idea}</title>
</head>
<body>
<h1>FAST BookSwap</h1>
<p>Campus marketplace for used books.</p>
<button>Join Waitlist</button>
</body>
</html>
"""

        Path("landing_page.html").write_text(html_content, encoding="utf-8")

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="result",
            payload={
                "result_type": "engineering_output",
                "status": "landing_page_created"
            },
            parent_message_id=latest_task["message_id"]
        )

        return response

    def handle_revision(self):
        messages = self.bus.get_messages_for_agent(self.name)

        revision_msg = None
        for msg in reversed(messages):
            if msg["message_type"] == "revision_request":
                revision_msg = msg
                break

        if not revision_msg:
            return None

        updated_html = """<!DOCTYPE html>
<html>
<head>
<title>FAST BookSwap</title>
</head>
<body>
<h1>FAST BookSwap</h1>
<p>Buy and sell books easily.</p>
<button>Join Now</button>
<p>Contact: fastbookswap@fast.edu.pk</p>
</body>
</html>
"""

        Path("landing_page.html").write_text(updated_html, encoding="utf-8")

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="confirmation",
            payload={
                "result_type": "revision_completed",
                "status": "Landing page updated"
            },
            parent_message_id=revision_msg["message_id"]
        )

        return response

    def create_github_issue(self, repo):
        try:
            issue = repo.create_issue(
                title="Initial landing page",
                body="Auto-created by Engineer agent to track landing page implementation."
            )
            return issue.html_url
        except Exception:
            issues = repo.get_issues(state="open")
            for i in issues:
                if i.title == "Initial landing page":
                    return i.html_url
            return None

    def create_github_pr(self):
        load_dotenv()

        token = os.getenv("GITHUB_TOKEN")
        repo_name = os.getenv("GITHUB_REPO")

        g = Github(token)
        repo = g.get_repo(repo_name)

        branch = "agent-update-landing"

        # create branch if not exists
        try:
            repo.create_git_ref(
                ref=f"refs/heads/{branch}",
                sha=repo.get_branch("main").commit.sha
            )
        except:
            pass

        content = Path("landing_page.html").read_text(encoding="utf-8")

        # create/update file
        try:
            repo.create_file(
                "landing_page.html",
                "Agent update",
                content,
                branch=branch
            )
        except:
            contents = repo.get_contents("landing_page.html", ref=branch)
            repo.update_file(
                contents.path,
                "Agent update",
                content,
                contents.sha,
                branch=branch
            )

        # create PR
        try:
            pr = repo.create_pull(
                title="Agent Update Landing Page",
                body="Auto PR by Engineer agent",
                head=branch,
                base="main"
            )
            pr_url = pr.html_url
        except Exception:
            pulls = repo.get_pulls(state='open', head=f"{repo.owner.login}:{branch}")
            pr_url = pulls[0].html_url if pulls.totalCount > 0 else "PR already exists"

        # create issue (NEW)
        issue_url = self.create_github_issue(repo)

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="confirmation",
            payload={
                "result_type": "github_artifacts",
                "pr_url": pr_url,
                "issue_url": issue_url
            }
        )

        return response