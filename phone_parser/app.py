from .helpers import loader
from .helpers import parser
from .helpers.config import ConfigParser


class App:

    def __init__(self):
        files_path = ConfigParser.config['APP']['FILES_PATH']
        files_ext = ConfigParser.config['APP']['FILES_EXT']
        self.loader = loader.FileLoader(files_path, files_ext)
        file_list = self.loader.generate_file_list()
        print('file list' + str(file_list))
        self.parser = parser.Parser(file_list)
        number_list = self.parser.get_number_list()
        print(number_list)
        final_list = self.parser.generate_formatted_list(number_list)
        print('final list')
        print(final_list)