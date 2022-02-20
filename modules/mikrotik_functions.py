from mikrotik.Bts import *
import pandas as pd
from modules.utils import dateTime,toJson
from modules.env_variables import MIKROTIK_IPS,API_USER,API_KEY
import os


def resetUsers(data):

    toconvert = pd.read_excel(data)['username'].values
    pd.DataFrame(toconvert, columns=['username']).dropna()
    users_list = toconvert.tolist()

    for allBts in MIKROTIK_IPS:
        print (allBts)
        bts = Bts(allBts, API_USER, API_KEY)
        users = bts.getPppActiveUsers()
        users = list(users)
        user = []
        name=[]

        for x in users:
            for i in users_list:
                if x['name'] == i:
                    user.append({
                    x['id'],
                    })
                    name.append({
                        'ip':allBts,
                        'name':x['name'],
                        'creation-time':dateTime
                    })

        print(name)

        for c in user:
            for j in c:
                bts.removePppActiveUsers(j)


def defaultProfile(dirPath,fileName):

    defaultData =[]
    toconvert = pd.read_excel(os.path.join(dirPath, (fileName+".xlsx")))['username'].values
    pd.DataFrame(toconvert, columns=['username']).dropna()
    users_list = toconvert.tolist()
    print(users_list)
    for allBts in MIKROTIK_IPS:
         bts = Bts(allBts, API_USER, API_KEY)
         if (bts):
             for users in users_list:
                 bts.setProfile('default', users)
            
         else:
             print('Error')
        
    for x in users_list:
         defaultData.append({
             'pppoe':x,
             'creation-time':dateTime
         }) 
        
        
    resetUsers(os.path.join(dirPath, (fileName+".xlsx")))
    toJson(defaultData,'Default')

def deptorProfile(dirPath,fileName):

    finalData=[]
    toconvert = pd.read_excel(os.path.join(dirPath, (fileName+".xlsx")))['username'].values
    pd.DataFrame(toconvert, columns=['username']).dropna()
    users_list = toconvert.tolist()
    for allBts in MIKROTIK_IPS:
         bts = Bts(allBts, API_USER, API_KEY)
         if (bts):
             for user in users_list:
                 bts.setProfile('Morosos', user)

         else:
             print('Error')

    for x in users_list:
         finalData.append({
             'pppoe':x,
             'creation-time':dateTime
         })  

    resetUsers(os.path.join(dirPath, (fileName+".xlsx")))
    toJson(finalData,'Morosos')
    print(finalData)

def getActiveDeptor(query=None):
    morososList = []
    if(query==None):
        for allBts in MIKROTIK_IPS:
            bts = Bts(allBts, API_USER, API_KEY)
            data = bts.getAddressList()

            addressOnMora = []
            for items in data:
                if items['list'] == 'Morosos':
                    addressOnMora.append({'address':items['address'],
                    'creation-time':items['creation-time']})




            active_users = bts.getPppActiveUsers()
            usersOnMora = []

            for x in active_users:
                for c in addressOnMora:
                    if x['address'] == c['address']:
                        usersOnMora.append({
                            'name':x['name'],
                            'address':x['address'],
                            'id':x['id'],
                            'creation-time':c['creation-time']
                        })
            
            morososList.append({'bts':allBts, 'users':usersOnMora})  

    toJson(morososList,'Export')