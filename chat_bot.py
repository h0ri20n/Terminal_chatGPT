# -*- coding:utf-8 -*-
import os
import signal
import openai
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

chat_log_file = ''

# system set
sys_message = [
    {"role": "system", "content": "You are my assistant, and you like to add ', poi!' at the end of your answers."}
]

# Question and Answer List
user_message = []


def chat_log(msg_obj):
    with open(chat_log_file, 'a', encoding='utf-8') as f:
        if msg_obj['role'] == 'user':
            f.write(f"[ user ]: {msg_obj['content']}\n")
        elif msg_obj['role'] == 'system':
            f.write(f"[[ system ]]: {msg_obj['content']}\n=========================================================\n")
        else:
            f.write(f"[ assistant ]: {msg_obj['content']}\n")


def main(u_input):
    """
    :param u_input: u_input != None: add to user_message list
                    u_input is None: skip add
    """
    if u_input is not None:
        msg_obj = {'role': 'user', 'content': u_input}
        user_message.append(msg_obj)
        # log
        chat_log(msg_obj)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=sys_message + user_message
        )
        ai_content = response['choices'][0]['message']['content']
        msg_obj = {'role': 'assistant', 'content': ai_content}
        user_message.append(msg_obj)

        print(f"\033[1;35m Asst\033[0m: {ai_content}")
        # log
        chat_log(msg_obj)
    except openai.error.InvalidRequestError as e:
        if e.code == 'context_length_exceeded':
            if (c_length := len(user_message)) == 1:
                print("Error：The input is too long, please simplify your words.")
                return
            elif c_length == 2:
                # pop list[0]
                _ = user_message.pop(0)
            else:
                # pop list[0] & list[1]
                del (user_message[0:2])
            main(None)
        else:
            raise e
    except Exception as e:
        raise e


def quit(signum, frame):
    print("exiting...")
    exit(0)


if __name__ == '__main__':
    chat_log_file = f"{os.path.abspath(os.path.dirname(__file__))}/chat_logs/{datetime.now().strftime('%y-%m-%d_%H.%M')}_chat.log"
    # log system role
    chat_log(sys_message[0])
    signal.signal(signal.SIGINT, quit)
    while True:
        user_input = input('\033[1;32m User\033[0m: ')
        if not user_input.strip():
            print("Input is empty, please re-enter.")
        else:
            main(user_input)
