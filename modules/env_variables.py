from dotenv import load_dotenv
import os

load_dotenv()

MIKROTIK_IPS = [
        #os.getenv('BTS_200'),
        #os.getenv('BTS_220'),
        #os.getenv('BTS_230'),
        os.getenv('BTS_MORON'),
        #os.getenv('BTS_CALERA'),
        os.getenv('BTS_TABUYO'),
        #os.getenv('BTS_BLANDON'),
        #os.getenv('BTS_IBERIA'),
        #os.getenv('BTS_GUAMAL'),
        #os.getenv('BTS_SUPIA'),
        #os.getenv('BTS_IRRAFO'),
        #os.getenv('BTS_IRRAINA'),
        #os.getenv('BTS_SL'),
        #os.getenv('BTS_CRUCES'),
        #os.getenv('BTS_PV')     
    ]
API_USER = os.getenv('API_USER')
API_KEY = os.getenv('API_KEY')

DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')