import sys
from .mutation import mutate
from .arguments import PassflipArgumentParser
from .input import prompt_password, prompt_salt, PromptError


def main():
    argument_parser = PassflipArgumentParser()
    arguments = argument_parser.parse_args()

    try:
        password = prompt_password(arguments.check)
    except PromptError as e:
        print(e)
        return -1

    while True:
        try:
            salt = prompt_salt(arguments.check)
        except PromptError as e:
            if arguments.multiple:
                break
            else:
                print(e)
                return -1
        output = mutate(password, salt)
        if arguments.length is not None:
            output = output[:int(arguments.length)]
        print(output)
        if not arguments.multiple:
            break
    return 0


def prompt_with_double_check():
    password = prompt_password()
    password_again = prompt_password(again=True)
    if password != password_again:
        print("Passwords do not match.")
        return
    salt = prompt_salt()
    salt_again = prompt_salt(again=True)
    if salt != salt_again:
        print("Salts do not match.")
        return
    return (password, salt)


def prompt_in_default_mode():
    password = prompt_password()
    salt = prompt_salt()
    return (password, salt)
