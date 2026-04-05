from message_bus import MessageBus


class ProductAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "Product"

    def process_task(self):
        messages = self.bus.get_messages_for_agent(self.name)
        if not messages:
            return None

        latest_task = messages[-1]
        startup_idea = latest_task["payload"].get("startup_idea", "Startup")

        product_spec = {
            "product_name": "FAST BookSwap",
            "startup_idea": startup_idea,

            "value_proposition":
                "A campus-first marketplace that helps students buy, sell, "
                "and exchange used academic books at affordable prices.",

            "target_users": "University students",

            "personas": [
                {
                    "name": "Ali - Budget Student",
                    "goal": "Find affordable textbooks",
                    "pain_point": "New books are expensive"
                },
                {
                    "name": "Sara - Final Year Student",
                    "goal": "Sell old books",
                    "pain_point": "No easy resale platform"
                },
                {
                    "name": "Usman - Freshman",
                    "goal": "Get course-specific material",
                    "pain_point": "Does not know seniors"
                }
            ],

            "ranked_features": [
                "Post used books",
                "Search by course",
                "Direct contact with seller",
                "Campus filtering",
                "Wishlist / alerts"
            ],

            "user_stories": [
                "As a student, I want to search books by course so I can find relevant material.",
                "As a seller, I want to post my used books so I can recover costs.",
                "As a buyer, I want to contact seller directly so I can negotiate price."
            ]
        }

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="result",
            payload={
                "result_type": "product_spec",
                "data": product_spec
            },
            parent_message_id=latest_task["message_id"]
        )

        return response