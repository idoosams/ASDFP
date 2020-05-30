import configparser

config = configparser.ConfigParser()
config['db'] = {'url': 'mongodb://mongo-asd:27017', }
config['mq'] = {'url': 'rabbitmq://mq-asd:5672', }
config["server"] = {'host': '0.0.0.0',
                    'port': '5000',
                    'fields': 'pose,color_image,feelings,depth_image'}
config["data"] = {'path': '../data'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)
