#!/usr/bin/python3

import click
from modules.mikrotik_functions import defaultProfile,deptorProfile
from pathlib import Path

@click.command()
@click.option('-p', '--profile',default='default', help='Perfiles (morosos-default)')
@click.option('-n', '--name',default='habilitar', help='Nombre del archivo')
@click.option('-d', '--dirname',default='Documents',help='Directorio del archivo a leer (Documents, Desktop, Downloads) por defecto es Documents')



def main (profile, name, dirname):
    dirPath = (Path.home() / dirname)
    if profile == 'default':
        defaultProfile(dirPath,name)
        #testing(dirPath,name)
    elif profile == 'morosos':
        deptorProfile(dirPath,name)
    else:
        print('Perfil no valido, Intente Nuevamente')



if __name__ == '__main__':
    main()
