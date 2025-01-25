import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")
# config = configparser.RawConfigParser()
# config.read(config.ini)

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url
    @staticmethod
    def getEmail():
        email = config.get('commonInfo', 'email')
        return email

    @staticmethod
    def getpasswd():
        passwd = config.get('commonInfo', 'passwd')
        return passwd

    @staticmethod
    def getRegDetails(where, what):
        details = config.get(where, what)
        return details


