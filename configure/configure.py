import ConfigParser

def get_class():
    Config = ConfigParser.ConfigParser()
    Config.read('configure/myfile.ini')
    # print Config
    # print Config.sections()
    sections = Config.sections()
    return Config.get('ClassImport', 'Name')

def get_class_name():
    Config = ConfigParser.ConfigParser()
    Config.read('configure/myfile.ini')
    sections = Config.sections()
    return Config.get('ClassImport', 'Class')