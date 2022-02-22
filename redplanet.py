#!/usr/bin/python3

from cgi import test
import click
from modules.utils import howToUse



class GroupExt(click.Group):
    def add_command(self, cmd, name=None):
        click.Group.add_command(self, cmd, name=name)
        for param in self.params:
            cmd.params.append(param)

howToUse()

@click.group()
def setProfileFromExcel():
    pass


@setProfileFromExcel.command()
@click.argument('profile')
@click.option('-d','--dir', default='Documents', help='Directorio donde se encuentra el archivo excel')
@click.option('-f','--file', default='habilitar', help='Nombre del archivo excel')

def Excel(profile, dir, file):
    print ('setProfile', profile,dir, file)


@click.group()
def setProfileFromSQL():
    pass

@setProfileFromSQL.command()
@click.argument('profile')
@click.option('-i','--id', help='Codigo del abonado', multiple=True)

def SQL(profile, id):
    data = list(map(int, list(id)))
    print (data,type(data))




@click.command(cls=click.CommandCollection, sources=[setProfileFromExcel, setProfileFromSQL])
def cli():
    pass



if __name__ == '__main__':
    cli(obj={})