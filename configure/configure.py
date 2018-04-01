import ConfigParser

def getClass():
    Config = ConfigParser.ConfigParser()
    Config.read('configure/myfile.ini')
    # print Config
    # print Config.sections()
    sections = Config.sections()
    return Config.get('ClassImport', 'Name')

def getClassName():
    Config = ConfigParser.ConfigParser()
    Config.read('configure/myfile.ini')
    sections = Config.sections()
    return Config.get('ClassImport', 'Class')