from agent_platform.memory.models import Memory

class MemoryService:

    def store(
        self,
        db,
        payload
    ):

        row = Memory(
            agent_name=payload["agent_name"],
            key=payload["key"],
            value=payload["value"]
        )

        db.add(row)
        db.commit()

        return row