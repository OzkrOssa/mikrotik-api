from sqlalchemy import create_engine
from decouple import config

USER = config('MYSQL_USER')
PASSWORD = config('MYSQL_PASSWORD')


engine = create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@35.226.203.230/redplanet')
conn = engine.connect()


def create():
    pass

def update():
    pass

def delete():
    pass

def findUsersbyAbonado(abonados=[]):

    if(len(abonados) == 1):
        result = engine.execute("SELECT PPPOE FROM usuarios WHERE N_ABONADOS={}".format(abonados))
        return print(result.fetchone()['PPPOE'])
    
    else:
        user = []
        for row in abonados:
            result = engine.execute("SELECT PPPOE FROM usuarios WHERE N_ABONADOS={}".format(row))
            res = result.fetchone()['PPPOE']
            res = " ".join(res.split())
            user.append(res)
        return print(user)

findUsersbyAbonado([434, 567, 890])
