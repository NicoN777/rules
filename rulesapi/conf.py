import configparser
from data.dbconn import DatabaseConnection
import os


ROOT = os.path.abspath(os.path.join(os.path.abspath(__file__), os.path.abspath(os.pardir)))
PROJECT_ROOT = os.path.dirname(os.path.join(ROOT, os.path.abspath(__file__)))
properties_file = os.environ.get('SECRET')
config = configparser.RawConfigParser()
config.read(properties_file)


#Database
db_name = config.get('Database', 'name')
print(ROOT)
database = str(os.path.abspath(os.path.join(ROOT, f'db/{db_name}')))
print(database)
connection = DatabaseConnection(name=database)

#Notifications
twilio_sid = str(config.get('Twilio', 'sid'))
twilio_token = str(config.get('Twilio', 'token'))
sender = str(config.get('Twilio', 'sender'))
receivers = [config.get('SMS', name) for name in config.options('SMS')]
