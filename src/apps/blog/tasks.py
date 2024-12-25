from apprise import Apprise

from core.taskiq import broker


@broker.task
async def send_notification_email(email: str) -> None:
    print(f"Sending notification email to {email}")

    apprise = Apprise()
    apprise.add("mailto://test@example.com")
    await apprise.async_notify(
        title="Test",
        body="Hello, world!",
    )
