from message_bus import MessageBus
from typing import Optional, Dict
import os
import json
from dotenv import load_dotenv
from google import genai


class CEOAgent:
    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.name = "CEO"
        load_dotenv()
        self.model = os.getenv("GEMINI_MODEL", "gemini-3-flash-preview")

    def _extract_json(self, text: str):
        if not text:
            return None

        cleaned = text.strip()

        if cleaned.startswith("```"):
            cleaned = cleaned.strip("`")
            if cleaned.lower().startswith("json"):
                cleaned = cleaned[4:].strip()

        try:
            return json.loads(cleaned)
        except Exception:
            return None

    def _fallback_plan(self, startup_idea: str) -> dict:
        return {
            "reasoning": (
                "Fallback reasoning: LLM unavailable.\n"
                "- Product: define value proposition, personas, features, and user stories\n"
                "- Engineer: build landing page and GitHub workflow\n"
                "- Marketing: create tagline, launch copy, email, and Slack message"
            ),
            "product_task": "Define the product specification with personas, features, and user stories.",
            "engineer_task": "Build a responsive landing page and prepare GitHub issue/PR workflow.",
            "marketing_task": "Create tagline, short description, cold email, and Slack launch message."
        }

    def _call_gemini(self, prompt: str) -> str:
        try:
            client = genai.Client()
            response = client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            return (response.text or "").strip()
        except Exception as e:
            print("Gemini error:", e)
            return ""

    def start_project(self, startup_idea: str):
        prompt = f"""
You are the CEO of a startup.

Startup idea:
{startup_idea}

Return a JSON object with exactly these keys:
{{
  "reasoning": "short explanation",
  "product_task": "task for Product agent",
  "engineer_task": "task for Engineer agent",
  "marketing_task": "task for Marketing agent"
}}

Make the tasks specific to the startup idea.
"""

        raw = self._call_gemini(prompt)
        parsed = self._extract_json(raw)

        if not parsed:
            parsed = self._fallback_plan(startup_idea)
            raw = parsed["reasoning"]

        self.bus.create_message(
            from_agent=self.name,
            to_agent="Product",
            message_type="task",
            payload={
                "startup_idea": startup_idea,
                "task": parsed.get("product_task", "Create product specification."),
                "llm_reasoning": parsed.get("reasoning", raw)
            }
        )

        self.bus.create_message(
            from_agent=self.name,
            to_agent="Engineer",
            message_type="task",
            payload={
                "startup_idea": startup_idea,
                "task": parsed.get("engineer_task", "Build landing page."),
                "llm_reasoning": parsed.get("reasoning", raw)
            }
        )

        self.bus.create_message(
            from_agent=self.name,
            to_agent="Marketing",
            message_type="task",
            payload={
                "startup_idea": startup_idea,
                "task": parsed.get("marketing_task", "Create marketing content."),
                "llm_reasoning": parsed.get("reasoning", raw)
            }
        )

    def handle_qa_feedback(self) -> Optional[Dict]:
        messages = self.bus.get_messages()

        qa_feedback = None
        for msg in reversed(messages):
            if msg["message_type"] == "result" and msg["payload"].get("result_type") == "qa_feedback":
                qa_feedback = msg
                break

        if not qa_feedback:
            return None

        feedback = qa_feedback["payload"]["feedback"]

        prompt = f"""
You are the CEO reviewing QA feedback.

QA feedback:
{feedback}

Return a JSON object with:
{{
  "decision": "YES or NO",
  "reasoning": "brief reasoning",
  "revision_instruction": "what the Engineer should change"
}}

If revision is needed, answer YES.
"""

        raw = self._call_gemini(prompt)
        parsed = self._extract_json(raw)

        if not parsed:
            parsed = {
                "decision": "YES",
                "reasoning": "Fallback decision: QA feedback indicates the landing page should be improved.",
                "revision_instruction": "Add a stronger CTA and include contact email."
            }

        decision = str(parsed.get("decision", "")).upper()
        reasoning = parsed.get("reasoning", raw or "No reasoning returned.")
        revision_instruction = parsed.get("revision_instruction", feedback)

        if "YES" in decision or "REVISE" in decision:
            return self.bus.create_message(
                from_agent=self.name,
                to_agent="Engineer",
                message_type="revision_request",
                payload={
                    "feedback": feedback,
                    "llm_decision": reasoning,
                    "revision_instruction": revision_instruction
                },
                parent_message_id=qa_feedback["message_id"]
            )

        return None