from sqlalchemy import create_engine
from modules.env_variables import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST


engine = create_engine(f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/redplanet')
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
