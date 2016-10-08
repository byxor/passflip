import sys
from getpass import getpass
from mutation import mutate


def main(argc, argv):

    if argc > 0 and argv[0] == "--help":
        display_help()
        exit(0)

    password = getpass("password: ")
    salt = getpass("salt: ")
    mutated = mutate(password, salt)

    print(mutated)


def display_help():
    print()
    print("usage: passflip <password> <salt>")
    print()
    print("You can use the salt to modify the result of the password mutator.")
    print()
    print("E.g.")
    print("If I wanted different passwords for Facebook and Twitter,")
    print("I would run passflip with the following standard input:")
    print()
    print("password: secret123")
    print("salt: facebook")
    print()
    print("and...")
    print()
    print("password: secret123")
    print("salt: twitter")
    print()


if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    main(argc, argv)

