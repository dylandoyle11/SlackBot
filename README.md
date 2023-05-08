# SlackBot
A Python package to send files and messages via Slack using the Slack API.

## Installation
To install the package, simply run:

Copy code
``'pip install slack-sdk``'
## Usage
To use the SlackBot class, first import the SlackBot class from the package:
``'from slackbot import SlackBot``'
Then, create an instance of the SlackBot class with your Slack bot token:


```
SLACK_BOT_TOKEN = 'xoxb-1234567890-1234567890123-abcdefghijklmnopqrstuvwxyz'
slack_bot = SlackBot(bot_token=SLACK_BOT_TOKEN)
```
You can then use the send_message, send_block, and send_file methods to send messages and files via Slack:

```
# Send a message to a channel
channels = ['#general']
messages = ['Hello from SlackBot!']
slack_bot.send_message(channels, messages)

# Send a block message to a channel
channels = ['#general']
blocks = [{'type': 'section', 'text': {'type': 'mrkdwn', 'text': 'Hello from SlackBot!'}}]
slack_bot.send_block(channels, blocks)

# Send a file to a channel
channels = ['#general']
files = ['example.txt']
titles = ['Example File']
slack_bot.send_file(channels, files, titles)
```

Note: Make sure to create a Slack bot and obtain a bot token before using the package. You can create a new bot and obtain a bot token by following the instructions in the Slack API documentation.
