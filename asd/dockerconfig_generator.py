import configparser
"""
Run to generate the defalt config needed for a docker deployment.
"""
config = configparser.ConfigParser()
config['db'] = {'url': 'mongodb://mongo-asd:27017', }
config['mq'] = {'url': 'rabbitmq://mq-asd:5672', }
config["server"] = {'host': '0.0.0.0',
                    'port': '5000',
                    'fields': 'datetime,pose,color_image,feelings,depth_image'}
config["api"] = {'host': '0.0.0.0',
                 'port': '8000'}
config["data"] = {'path': '../data'}
with open('dockerconfig.ini', 'w') as configfile:
    config.write(configfile)
