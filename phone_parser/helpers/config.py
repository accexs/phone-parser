import configparser


class ConfigParser:

    config = configparser.ConfigParser()
    config.read('phone_parser/config/config.ini')
