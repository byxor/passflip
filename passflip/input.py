from getpass import getpass


def create_prompt_message(message, again=False):
    prompt_message = message
    if again:
        prompt_message += " again"
    prompt_message += ": "
    return prompt_message


def prompt(message, again=False):
    prompt_message = create_prompt_message(message, again)
    return getpass(prompt_message)


def prompt_password(again=False):
    return prompt("enter password", again)


def prompt_salt(again=False):
    return prompt("enter salt", again)

