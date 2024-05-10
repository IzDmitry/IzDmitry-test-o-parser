import os

# any configuration should be stored here
TOKEN = os.environ.get('BOT_TOKEN')
#TOKEN = '5998336317:AAHzoVA_fmFPTOLsa1g5RrVcb0z_OlQNPx4'

MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PORT = 3306
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_ROOT_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')
MYSQL_DB = os.environ.get('MYSQL_DB')

print(MYSQL_DB)