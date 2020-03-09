# content of test_loader.py
import pytest
from phone_parser.helpers.loader import FileLoader
from phone_parser.helpers.config import ConfigParser

files_path = ConfigParser.config['APP']['FILES_PATH']
files_ext = ConfigParser.config['APP']['FILES_EXT']
loader = FileLoader(files_path, files_ext)


def test_loader():
    assert type(loader.files_path) is str
    assert type(loader.files_ext) is str
    file_list = loader.generate_file_list()
    assert type(file_list) is list
