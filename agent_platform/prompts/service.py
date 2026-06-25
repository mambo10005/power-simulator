from agent_platform.prompts.models import Prompt

class PromptService:

    def create(
        self,
        db,
        payload
    ):

        row = Prompt(
            name=payload["name"],
            content=payload["content"]
        )

        db.add(row)
        db.commit()

        return row