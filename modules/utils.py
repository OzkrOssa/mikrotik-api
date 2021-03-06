import os
from datetime import datetime
from pathlib import Path
import json


dateTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
date = datetime.now().strftime("%d_%m_%Y")

#funcion que recibe una data y la guarda en un archivo json
def toJson(data,fileName):
    dirPathExport = str(Path.home()/'Documents')
    file = date+'_'+fileName+'.json'
    with open(os.path.join(dirPathExport, (file)), 'w') as file:
                json.dump(data, file)