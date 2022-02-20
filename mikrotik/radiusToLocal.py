from Bts import *
from modules.env_variables import MIKROTIK_IPS,API_KEY,API_USER

for allBts in MIKROTIK_IPS:
    bts= Bts(allBts, API_USER, API_USER)
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
