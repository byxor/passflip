import sys
from .mutation import mutate
from .arguments import PassflipArgumentParser
from .input import prompt_password, prompt_salt


def main():
    argument_parser = PassflipArgumentParser()
    arguments = argument_parser.parse_args()

    password = prompt_password(arguments.check)

    while True:
        salt = prompt_salt(arguments.check)

        if password is None or salt is None:
            return

        output = mutate(password, salt)

        if arguments.length is not None:
            output = output[:int(arguments.length)]

        print(output)

        if salt is None or not arguments.multiple:
            break


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
