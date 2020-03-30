import pathlib
import slack

with open(pathlib.Path(__file__).parent / "token.key", "r") as token_file:
    token = token_file.read().strip()
with open(pathlib.Path(__file__).parent / "message.md", "r") as message_file:
    message = message_file.read().strip()
with open(pathlib.Path(__file__).parent / "users.list", "r") as user_file:
    users = filter(None, user_file.read().split("\n"))

for user in users:
    slack.WebClient(token).chat_postMessage(
        text=message,
        channel=user,
        as_user=True,
        )
