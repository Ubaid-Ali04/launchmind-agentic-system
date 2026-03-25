from message_bus import MessageBus


class MarketingAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "Marketing"

    def process_task(self):
        """
        Read marketing task and generate marketing content.
        """
        messages = self.bus.get_messages_for_agent(self.name)
        if not messages:
            print("No messages for Marketing agent.")
            return None

        latest_task = messages[-1]
        startup_idea = latest_task["payload"].get("startup_idea", "FAST BookSwap")

        marketing_content = {
            "tagline": "Buy, Sell, and Swap Study Materials — All Within FAST.",
            "social_post": (
                "Tired of expensive textbooks? 📚 FAST BookSwap lets you buy, sell, "
                "and exchange books and notes with fellow students. Join the waitlist today!"
            ),
            "cold_email": (
                "Subject: Introducing FAST BookSwap\n\n"
                "Hi there,\n\n"
                "We're launching FAST BookSwap — a simple campus marketplace for students "
                "to exchange books, notes, and study materials.\n\n"
                "Save money and help fellow students succeed.\n\n"
                "Join the waitlist today.\n\n"
                "Best,\n"
                "FAST BookSwap Team"
            ),
            "slack_message": (
                "*FAST BookSwap Launch 🚀*\n"
                "Buy, sell, and exchange study materials within campus.\n"
                "Join the waitlist and start saving today!"
            )
        }

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="marketing_output",
            payload=marketing_content,
            parent_message_id=latest_task["message_id"]
        )

        return response