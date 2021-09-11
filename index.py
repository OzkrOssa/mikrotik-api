from Bts import *
import json
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

now = datetime.now()
load_dotenv()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

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

def toJson(data,fileName):
    dir='C:/Users/Servicio al Cliente/Desktop'
    file_name = fileName+".json"
    
    with open(os.path.join(dir, file_name), 'w') as file:
                json.dump(data, file)
def resetUsers(data):
    toconvert = pd.read_excel(data+'.xlsx')
    listado = toconvert['username'].values
    df = pd.DataFrame(listado, columns=['username'])
    test = df.dropna()
    test.to_excel(data+'1.xlsx', sheet_name=data)
    archivo_excel = pd.read_excel(data+'1.xlsx')
    lista = archivo_excel['username'].values
    users_list = lista.tolist()

    for allBts in IPS:
        print (allBts)
        bts = Bts(allBts, 'api', '1017230619')
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
                        'creation-time':dt_string
                    })

        print(name)

        for c in user:
            for j in c:
                bts.removePppActiveUsers(j)

def defaultProfile():
    defaultData =[]
    toconvert = pd.read_excel('habilitar.xlsx')
    listado = toconvert['username'].values
    df = pd.DataFrame(listado, columns=['username'])
    test = df.dropna()
    test.to_excel('habilitar1.xlsx', sheet_name='habilitar')
    archivo_excel = pd.read_excel('habilitar1.xlsx')
    lista = archivo_excel['username'].values
    users_list = lista.tolist()
    for allBts in IPS:
        bts = Bts(allBts, 'api', '1017230619')
        if (bts):
            for users in users_list:
                bts.setProfile('default', users)
            
        else:
            print('Error')
        
    for x in users_list:
        defaultData.append({
            'pppoe':x,
            'creation-time':dt_string
        }) 
        
        
    resetUsers('habilitar')
    toJson(defaultData,'Default')

def deptorProfile():
    finalData=[]
    toconvert = pd.read_excel('morosos.xlsx')
    listado = toconvert['username'].values
    df = pd.DataFrame(listado, columns=['username'])
    test = df.dropna()
    test.to_excel('morosos1.xlsx', sheet_name='morosos')
    archivo_excel = pd.read_excel('morosos1.xlsx')
    lista = archivo_excel['username'].values
    users_list = lista.tolist()
    for allBts in IPS:
        bts = Bts(allBts, 'api', '1017230619')
        if (bts):
            for user in users_list:
                bts.setProfile('Morosos', user)

        else:
            print('Error')
    for x in users_list:
        finalData.append({
            'pppoe':x,
            'creation-time':dt_string
        })  

    resetUsers('morosos')
    toJson(finalData,'Morosos')
    print(finalData)

def getActiveDeptor(query=None):
    morososList = []
    if(query==None):
        for allBts in IPS:
            bts = Bts(allBts, 'api', '1017230619')
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

getActiveDeptor()
#deptorProfile()
#defaultProfile()