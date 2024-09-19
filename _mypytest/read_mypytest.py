"""Reads mypytest.ini"""

import configparser
from pathlib import Path


CG_FILE = "mypytest.ini"

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(CG_FILE)
config.read(CONFIG_FILE)


def get_mytest_dir():
    """GET"""
    return config["tests"]["dir"]


def get_mytest_files():
    """GET"""
    return config["tests"]["files"]


def get_version():
    return config["framework"]["version"]


def get_mytest_classes():
    return config["tests"]["classes"]


def get_mytest_funcs():
    return config["tests"]["funcs"]
