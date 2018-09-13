""" main

Chatbot ShortyZwei

Author: datadonk23
Date: 13.09.18 
"""

from rasa_core.agent import Agent
import time


def cli_chat():
    """ Chat on CLI with bot

    :return: -
    """
    message = ["Hi, I'm ShortyZwei! Type 'stop' to end the conversation."]
    agent = Agent.load("models/dialogue", interpreter="models/current/nlu")

    while True:
        print(message)
        time.sleep(0.3)
        user_input = input()
        if user_input == "stop":
            break
        responses = agent.handle_message(user_input)
        for response in responses:
            message = response.get("text")


if __name__ == '__main__':
    cli_chat()
