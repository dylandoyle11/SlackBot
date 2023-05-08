"""
------------------------------------------------------------------------
Module to send files and messages via Slack
------------------------------------------------------------------------
Author(s): Dylan Doyle
Updated: 2020-12-19
------------------------------------------------------------------------
Notes:

INSTALL INSTRUCTIONS:

Clone repository to the same directory as the repository for the required script. They should
both exist within separate folders. Copy paste the following to import:

try:
    sys.path.insert(1, os.path.join('..', 'SlackBot')) ----> Directory will need to be customized per script
    from SlackBot import *
except ImportError as e :
    print('Cannot import SlackBot. Either it is not installed or the path "../SlackBot/" does not point to it.')
    print(e)
    exit(0)

------------------------------------------------------------------------
"""

import os
from slack_sdk import WebClient


class SlackBot:
    """
    A class to send files and messages via Slack.

    Attributes:
    -----------
    client : WebClient
        A Slack WebClient instance with the provided bot token.

    Methods:
    --------
    __init__(bot_token: str)
        Initializes a SlackBot instance with the provided bot token.
    send_message(channels: list, messages: list)
        Sends Slack message(s) to specified channel(s).
    send_block(channels: list, blocks: list)
        Sends Slack block message(s) to specified channel(s).
    send_file(channels: list, files: list, titles: list)
        Sends file(s) to specified channel(s).
    """

    def __init__(self, bot_token: str):
        """
        Initializes a SlackBot instance with the provided bot token.

        Parameters:
        -----------
        bot_token : str
            The Slack bot token to be used for sending messages and files.
        """
        self.client = WebClient(token=bot_token)


    def send_message(self, channels: list, messages: list):
        """
        Sends Slack message(s) to specified channel(s).

        Parameters:
        -----------
        channels : list
            List of channels to send messages to via Slack.
        messages : list
            List of messages to send.
        """
        for channel in channels:
            for message in messages:
                response = self.client.chat_postMessage(channel=channel, text=message)


    def send_block(self, channels: list, blocks: list):
        """
        Sends Slack block message(s) to specified channel(s).

        Parameters:
        -----------
        channels : list
            List of channels to send messages to via Slack.
        blocks : list
            List of blocks to send.
        """
        for channel in channels:
            for block in blocks:
                response = self.client.chat_postMessage(channel=channel, block=block)


    def send_file(self, channels: list, files: list, titles: list):
        """
        Sends file(s) to specified channel(s).

        Parameters:
        -----------
        channels : list
            List of channels to send files to via Slack.
        files : list
            List of files to send.
        titles : list
            List of titles of files. Titles should correspond to the same
            order of items in files list.
        """
        for channel in channels:
            for file, title in zip(files, titles):
                self.client.files_upload(channels=channel, file=file, title=title)


if __name__ == '__main__':

    # Initialize SlackBot instance
    SLACK_BOT_TOKEN = 'xoxb-4950217216-1580739024241-KE4CsYwOouHLxmpuEmk8BYJ4'
    slack_bot = SlackBot(bot_token=SLACK_BOT_TOKEN)

    # Example usage
    channels = ['#general']
    messages = ['Hello from SlackBot!']
    slack_bot.send_message(channels, messages)


