from getpass import getpass


class PromptError(Exception):
    """
    Raise this error if the user inputs something invalid

    eg: raise PromptError("you're input is whack yo")
    """


def prompt_input(message, validate):
    first_input = getpass(message + ': ')
    if len(first_input) == 0:
        raise PromptError("error: cannot enter empty string")
    if not validate:
        return first_input
    second_input = getpass(message + ' again: ')
    if first_input != second_input:
        raise PromptError("error: mismatching input")
    return first_input


def prompt_password(validate):
    return prompt_input("enter password", validate)


def prompt_salt(validate):
    return prompt_input("enter salt", validate)
