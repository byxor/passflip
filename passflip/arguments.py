from argparse import ArgumentParser


class PassflipArgumentParser(ArgumentParser):

    def __init__(self):
        super().__init__()
        self.init_arguments()

    def init_arguments(self):
        self.add_argument(
            "-c",
            "--check",
            action='store_true',
            help="prompt for password & salt twice."
        )

