from .config import ConfigParser


class Parser:
    def __init__(self, file_list):
        self.file_list = file_list
        self.def_a_code = ConfigParser.config['PARSER']['DEFAULT_A_CODE']
        self.def_c_code = ConfigParser.config['PARSER']['DEFAULT_C_CODE']

    def get_number_list(self):
        number_list = list()
        for file in self.file_list:
            number_list = [line.rstrip('\n') for line in open(file)]

        return number_list

    def parse_number(self, number):
        if not self.valid_number(number):
            raise Exception('Not a valid number')

        clean_number = self.clean_number(number)
        return self.complete_clean_number(str(clean_number))

    def valid_number(self, number):
        clean_number = str(self.clean_number(number))
        if len(clean_number) < 7:
            return False
        return True

    @staticmethod
    def clean_number(number):
        number = number.replace(' ', '')
        number = number.replace('-', '')
        number = number.replace('+', '')
        number = number.replace('(', '')
        number = number.replace(')', '')
        return number

    def sort_list(self, number_list):
        unique_list = list(set(number_list))
        sorted_list = list(map(self.clean_number, unique_list))
        sorted_list.sort()
        sorted_list = list(map(self.return_formatted_number, sorted_list))
        return sorted_list

    def complete_clean_number(self, clean_number):
        if len(clean_number) == 7:
            return self.def_c_code + self.def_a_code + clean_number
        elif 7 < len(clean_number) <= 10:
            body = clean_number[-7:]
            a_code = clean_number[-10:-7:]
            return self.def_c_code + a_code + body
        elif len(clean_number) > 10:
            return clean_number

    def generate_formatted_list(self, number_list):
        formatted_list = list()
        for number in number_list:
            formatted_list.append(self.parse_number(number))
        return self.sort_list(formatted_list)

    @staticmethod
    def return_formatted_number(clean_number):
        clean_number = str(str(clean_number))
        body = clean_number[-7:]
        a_code = clean_number[-10:-7:]
        c_code = clean_number[:-10:]
        return '+' + c_code + ' (' + a_code + ') ' + body[:3] + '-' + body[3:]
