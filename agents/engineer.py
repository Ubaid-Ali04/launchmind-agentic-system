from message_bus import MessageBus
from pathlib import Path


class EngineerAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "Engineer"

    def process_task(self):
        """
        Read the latest message assigned to Engineer and generate a landing page.
        """
        messages = self.bus.get_messages_for_agent(self.name)
        if not messages:
            print("No messages for Engineer agent.")
            return None

        latest_task = messages[-1]
        startup_idea = latest_task["payload"].get("startup_idea", "FAST BookSwap")

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{startup_idea}</title>
</head>
<body>
    <h1>FAST BookSwap</h1>
    <p>A simple campus marketplace for buying, selling, and exchanging used books.</p>
    <button>Join Waitlist</button>
</body>
</html>
"""

        output_file = Path("landing_page.html")
        output_file.write_text(html_content, encoding="utf-8")

        response_payload = {
            "status": "landing_page_created",
            "file_path": str(output_file),
            "summary": "Created landing page"
        }

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="engineering_output",
            payload=response_payload,
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

        feedback = revision_msg["payload"]["feedback"]

        updated_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>FAST BookSwap</title>
</head>
<body>
    <h1>FAST BookSwap</h1>
    <p>Buy, Sell, and Swap study materials within campus.</p>

    <h2>Why use FAST BookSwap?</h2>
    <ul>
        <li>Affordable textbooks</li>
        <li>Course-specific notes</li>
        <li>Connect with students</li>
    </ul>

    <button>Join Waitlist Now</button>

    <p>Contact: fastbookswap@fast.edu.pk</p>

    <hr>
    <small>Updated after QA feedback: {feedback}</small>
</body>
</html>
"""

        with open("landing_page.html", "w", encoding="utf-8") as f:
            f.write(updated_html)

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="revision_completed",
            payload={"status": "Landing page updated after QA feedback"},
            parent_message_id=revision_msg["message_id"]
        )

        return response