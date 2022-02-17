#!/usr/bin/python3

from cgi import test
import click
import ast

class GroupExt(click.Group):
    def add_command(self, cmd, name=None):
        click.Group.add_command(self, cmd, name=name)
        for param in self.params:
            cmd.params.append(param)



@click.group()
def byExcel():
    pass


@byExcel.command()
@click.argument('profile')
@click.option('-d','--dir', default='Documents', help='Directorio donde se encuentra el archivo excel')
@click.option('-f','--file', default='Documents', help='Nombre del archivo excel')
def fromExcel(profile, dir, file):
    print ('setProfile', profile,dir, file)


@click.group()
def bySQL():
    pass

@bySQL.command()
@click.argument('profile')
@click.option('-i','--id', help='Codigo del abonado', multiple=True)
@click.option('-f','--file', default='Documents', help='Nombre del archivo excel')

def fromSQL(profile, id, file):
    data = list(map(int, list(id)))



@click.command(cls=click.CommandCollection, sources=[byExcel, bySQL])
def cli():
    print ('cli')



if __name__ == '__main__':
    cli(obj={})