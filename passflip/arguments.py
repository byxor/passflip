from argparse import ArgumentParser


class PassflipArgumentParser(ArgumentParser):

    def __init__(self):
        super(PassflipArgumentParser, self).__init__()
        self.init_arguments()

    def init_arguments(self):
        self.add_argument(
            "-c",
            "--check",
            action="store_true",
            help="prompt for password & salt twice."
        )
        self.add_argument(
            "-m",
            "--multiple",
            action="store_true",
            help="prompt forever until input is blank"
        )
        self.add_argument(
            "-l",
            "--length",
            action="store",
            nargs="?",
            help="limit the length of the output password"
        )
