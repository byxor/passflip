import sys
from .mutation import mutate
from .arguments import PassflipArgumentParser
from .input import prompt_password, prompt_salt

def main():
    argument_parser = PassflipArgumentParser()
    arguments = argument_parser.parse_args()
    if arguments.check is True:
        mutated = run_with_double_check()
    else:
        mutated = run_in_default_mode() 


def run_with_double_check():
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
    print(mutate(password, salt))


def run_in_default_mode():
    password = prompt_password()
    salt = prompt_salt()
    print(mutate(password, salt))

