from agent_platform.registry.models import Agent

class AgentService:

    def create_agent(
        self,
        db,
        payload
    ):

        agent = Agent(
            name=payload["name"],
            role=payload["role"],
            model=payload["model"],
            status="ACTIVE"
        )

        db.add(agent)
        db.commit()
        db.refresh(agent)

        return {
            "id": agent.id,
            "name": agent.name,
            "role": agent.role,
            "model": agent.model,
            "status": agent.status
        }