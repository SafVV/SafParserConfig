import os
import configparser

# Тут парсер KeyWB ади из общей папки

def startParseFile():
    """Забирает значение ключа ВБ из общего файла в аппдата"""
    pt = os.getenv('APPDATA')
    if not os.path.exists(pt + '\SAF_DEV'):
        os.mkdir(pt + '\SAF_DEV')

    if not os.path.exists(pt + r'\SAF_DEV\global.ini'):
        text_file = open(pt + r'\SAF_DEV\global.ini', "w")
        text_file.close()
        config = configparser.ConfigParser()
        config.add_section('autotrade')
        config.set('autotrade', 'KeyAPI', "3333")

        with open(pt + r'\SAF_DEV\global.ini', "w") as configfile:
            config.write(configfile)
            print('Создал папку в %appdata% Roaming ')

    config = configparser.ConfigParser()
    config.read(pt + r'\SAF_DEV\global.ini')

    if not config.has_section('autotrade'):
        config.add_section('autotrade')
        config.set('autotrade', 'KeyAPI', "3333")

        with open(pt + r'\SAF_DEV\global.ini', "w") as configfile:
            config.write(configfile)
            print('Создал папку в %appdata% Roaming ')

    KeyAPI = config.get("autotrade", "KeyAPI")
    return KeyAPI


def setConfig(KeyApi):
    """СОхраняет значение ключа в общий фаил аппдата"""
    pt = os.getenv('APPDATA')
    config = configparser.ConfigParser()
    config.read(pt + r'\SAF_DEV\global.ini')
    config.set('autotrade', 'KeyAPI', str(KeyApi))
    with open(pt + r'\SAF_DEV\global.ini', "w") as config_file:
        config.write(config_file)
