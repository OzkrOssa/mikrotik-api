#!/usr/bin/python3

import click
import ast

class GroupExt(click.Group):
    def add_command(self, cmd, name=None):
        click.Group.add_command(self, cmd, name=name)
        for param in self.params:
            cmd.params.append(param)

class PythonLiteralOption(click.Option):
    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


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
@click.option('-id','--id',help='Directorio donde se encuentra el archivo excel')
@click.option("--format", multiple=True,default=[])
@click.option('-f','--file', default='Documents', help='Nombre del archivo excel')
def fromSQL(profile, id, file, format):
    print ('setSQL', file, id, profile)



@click.command(cls=click.CommandCollection, sources=[byExcel, bySQL])
def cli():
    print ('cli')



if __name__ == '__main__':
    cli(obj={})