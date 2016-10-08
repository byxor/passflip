import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open("passflip/passflip.py").read(),
    re.M
).group(1)


with open("README.md", "rb") as f:
    long_description = f.read().decode("utf-8")

setup(
    name = "cmdline-passflip",
    packages = ["passflip"],
    entry_points = {
        "console_scripts": ["passflip = passflip.passflip:main"]
    },
    version = version,
    description = "Command line tool to mutate passwords for different websites.",
    long_description = long_description,
    author = "Brandon Ibbotson",
    author_email = "brandon.ibbotson2@mail.dcu.ie",
    url = "https://www.github.com/byxor/passflip"
)

