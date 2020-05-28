import configparser

config = configparser.ConfigParser()
config['db'] = {'url': 'rabbitmq://mq-asd:5672', }
config['mq'] = {'url': 'rabbitmq://mq-asd:5672', }
config["server"] = {'host': '0.0.0.0',
                    'port': '5000'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)