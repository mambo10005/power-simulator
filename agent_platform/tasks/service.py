from agent_platform.tasks.models import Task

class TaskService:

    def submit(
        self,
        db,
        payload
    ):

        task = Task(
            agent_name=payload["agent_name"],
            task_type=payload["task_type"],
            prompt=payload["prompt"],
            status="QUEUED"
        )

        db.add(task)
        db.commit()

        return task