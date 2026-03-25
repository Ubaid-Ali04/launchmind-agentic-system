from message_bus import MessageBus


class QAAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "QA"

    def review_outputs(self):
        messages = self.bus.get_messages()

        engineering_output = None
        marketing_output = None

        for msg in messages:
            if msg["message_type"] == "engineering_output":
                engineering_output = msg
            if msg["message_type"] == "marketing_output":
                marketing_output = msg

        feedback_points = []

        if engineering_output:
            feedback_points.append(
                "Landing page should include contact email and stronger CTA button."
            )

        if marketing_output:
            feedback_points.append(
                "Marketing copy can include urgency like limited-time access."
            )

        feedback_text = " | ".join(feedback_points)

        response = self.bus.create_message(
            from_agent=self.name,
            to_agent="CEO",
            message_type="qa_feedback",
            payload={"feedback": feedback_text},
        )

        return response