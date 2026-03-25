from message_bus import MessageBus


class ProductAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "Product"

    def process_task(self):
        """
        Read the latest message assigned to Product and generate product specs.
        """
        messages = self.bus.get_messages_for_agent(self.name)
        if not messages:
            print("No messages for Product agent.")
            return None

        latest_task = messages[-1]
        startup_idea = latest_task["payload"].get("startup_idea", "Unknown idea")

        product_spec = {
            "product_name": "FAST BookSwap",
            "startup_idea": startup_idea,
            "target_users": "FAST students who want to buy, sell, or exchange used books, notes, and study materials.",
            "problem_statement": "Students often struggle to find affordable and relevant academic resources within campus.",
            "value_proposition": "A simple campus marketplace for exchanging study materials quickly and affordably.",
            "core_features": [
                "Post books and notes for sale or exchange",
                "Search and filter by course, semester, and category",
                "Direct contact between buyers and sellers",
                "Simple listing cards for easy browsing"
            ],
            "user_flow": [
                "User signs in with campus identity",
                "User browses listings",
                "User posts an item or contacts a seller",
                "User arranges exchange or purchase"
            ]
        }

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="product_spec",
            payload=product_spec,
            parent_message_id=latest_task["message_id"]
        )

        return response