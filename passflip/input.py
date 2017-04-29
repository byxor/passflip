from getpass import getpass


def prompt(message, validate):
    first_input = getpass(message + ': ')
    if len(first_input) == 0:
        return None
    if not validate:
        return first_input
    second_input = getpass(message + 'again: ')
    if first_input != second_input:
        first_input = None
    return first_input


def prompt_password(validate):
    return prompt("enter password", validate)


def prompt_salt(validate):
    return prompt("enter salt", validate)
