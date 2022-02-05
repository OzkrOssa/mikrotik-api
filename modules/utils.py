import os
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
import json

load_dotenv()

IPS = [
        os.getenv('BTS_200'),
        os.getenv('BTS_220'),
        os.getenv('BTS_230'),
        os.getenv('BTS_MORON'),
        os.getenv('BTS_CALERA'),
        os.getenv('BTS_TABUYO'),
        os.getenv('BTS_BLANDON'),
        os.getenv('BTS_IBERIA'),
        os.getenv('BTS_GUAMAL'),
        os.getenv('BTS_AFRICA'),
        os.getenv('BTS_SUPIA'),
        os.getenv('BTS_IRRAFO'),
        os.getenv('BTS_IRRAINA'),
        os.getenv('BTS_SL'),
        os.getenv('BTS_CRUCES'),
        os.getenv('BTS_PV')      
    ]


dateTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

#funcion que recibe una data y la guarda en un archivo json
def toJson(data,fileName):
    dirPathExport = str(Path.home()+'/Documents')
    with open(os.path.join(dirPathExport, (fileName+".json")), 'w') as file:
                json.dump(data, file)

print (os.getenv(TITLE))