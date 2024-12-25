from core.taskiq import broker


@broker.task
async def send_notification_email(email: str) -> None:
    print(f"Sending notification email to {email}")
