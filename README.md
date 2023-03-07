### Terminal_chatGPT
Chatting with chatGPT in the terminal.

- gpt-3.5-turbo
- Contextual association
- Simple max-token exception handling： Remove the earliest conversation.
- chat log

### Getting Started
1. Edit the `.env` file and fill in your `openAI API Key`.
2. Dependence：
    ```shell
    pip install -r requirements.txt
    ```
3. Customize your assistant in `chat_bot.py` file:
   ```python
   # system set
   sys_message = [
       {"role": "system", "content": "< Set your role >"}
   ]
   ```
4. run chat_bot.py
   ```shell
   python chat_bot.py
   ```
5. Simple registration to terminal command (Linux)：
   ```shell
   # Edit the .bashrc file under the home directory and add the following content at the end：
   # "alias chat='<Absolute path of python in virtual env> <Absolute path of the chat_bot.py file>'"
   
   # e.g.: 
   vim ~/.bashrc
   # add the following content && save
   alias chat='/home/test/Obj/Terminal_chatGPT/env/bin/python /home/test/Obj/Terminal_chatGPT/chat_bot.py'
   # apply
   source ~/.bashrc
   # try typing 'chat' in terminal
   ```
