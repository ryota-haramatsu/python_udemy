# config.iniを作成する

import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug': True
}
config['web_server'] = {
    'host': '127.0.0.1',
    'port': 80
}
config['db_server'] = {
    'host': '127.0.0.1',
    'port': 3306
}
with open('config.ini', 'w') as config_file:
    config.write(config_file)

# config.read('config.ini')をして config['web_server']['host']などとすると出力される
# config.read('config.ini')
# print(config['web_server']['port'])
