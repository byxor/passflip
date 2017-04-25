import sys
from .mutation import mutate
from .arguments import PassflipArgumentParser
from .input import prompt_password, prompt_salt


def main():
    argument_parser = PassflipArgumentParser()
    arguments = argument_parser.parse_args()

    if arguments.check is True:
        input_ = prompt_with_double_check()
    else:
        input_ = prompt_in_default_mode()

    if input_ is None:
        return

    output = mutate(input_[0], input_[1])

    if arguments.length is not None:
        output = output[:int(arguments.length)]

    print(output)


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
