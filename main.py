from mikrotik.Bts import *
from modules.functions import defaultProfile,deptorProfile


@click.group()
def cli():
    pass

@cli.command()
def default():
    defaultProfile()

@cli.command()
def deptor():
    deptorProfile()

if __name__ == '__main__':
    cli()
