from Bts import *
import os
from dotenv import load_dotenv


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

load_dotenv()
for allBts in IPS:
    bts= Bts(allBts, 'api', '1017230619')
    users = bts.getPppActiveUsers()
    users = list(users)

    userRadiusTrue =[]

    for x in users:
        if x['radius']=='true':
            userRadiusTrue.append({
                x['name']
                })

    for x in userRadiusTrue:
        for users in x:
            print (users)
            bts.createSecretUser(users)


    print (len(userRadiusTrue))
