import re
from setuptools import setup


with open("README.rst", "rb") as f:
    long_description = f.read().decode("utf-8")


setup(
    name = "passflip",
    packages = ["passflip"],
    entry_points = """
        [console_scripts]
        passflip=passflip.passflip:main
    """,
    license = "GPLv3",
    version = "0.5.7",
    description = "Command line tool to mutate passwords for different websites.",
    long_description = long_description,
    author = "Brandon Ibbotson",
    author_email = "brandon.ibbotson2@mail.dcu.ie",
    url = "https://www.github.com/byxor/passflip"
)

