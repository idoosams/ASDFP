import configparser
"""
Run to generate the defalt config needed for a local E2E run.
"""
config = configparser.ConfigParser()
config['db'] = {'url': 'mongodb://127.0.0.1:27017', }
config['mq'] = {'url': 'rabbitmq://127.0.0.1:5672', }
config["server"] = {'host': '127.0.0.1',
                    'port': '5000',
                    'fields': 'datetime,pose,color_image,feelings,depth_image'}
config["api"] = {'host': '127.0.0.1',
                 'port': '8000'}
config["data"] = {'path': '../data'}
with open('localconfig.ini', 'w') as configfile:
    config.write(configfile)
