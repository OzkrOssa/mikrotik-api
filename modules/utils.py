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

banner =('''

        _____  ______ _____  _____  _               _   _ ______ _______ 
        |  __ \|  ____|  __ \|  __ \| |        /\   | \ | |  ____|__   __|
        | |__) | |__  | |  | | |__) | |       /  \  |  \| | |__     | |   
        |  _  /|  __| | |  | |  ___/| |      / /\ \ | . ` |  __|    | |   
        | | \ \| |____| |__| | |    | |____ / ____ \| |\  | |____   | |   
        |_|  \_\______|_____/|_|    |______/_/    \_\_| \_|______|  |_|   
                                                                   
        CLI tool for management pppoe profiles on mikrotik routerOS
        Oscar Ossa                          

''')

def howToUse():
    print(banner)
    print('''
    NAME
    \t REDPLANETCLI.py - PPPOE profile manager for MikroTik devices\n
    USAGE
    \t python redplanet.py excel [profile] [-d] [-f]\n
    \t python redplanet.py sql [profile] [-i]\n
    OPTIONS
    \t [profile] \t\t Perfil que desea asociar al PPPOE (habilitar|morosos)
    \t -d, --dir \t\t Directorio donde se encuentra el archivo excel (default: ~/Documents)
    \t -f, --file \t\t Nombre del archivo excel (default: habilitar.xlsx)
    \t -i, --id \t\t Codigo del abonado
    ''')
