from dotenv import load_dotenv
import os

load_dotenv()

MIKROTIK_IPS = [
        os.getenv('BTS_MORON')   
    ]
API_USER = os.getenv('API_USER')
API_KEY = os.getenv('API_KEY')

DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')