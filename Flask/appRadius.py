from flask import Flask, request, jsonify
from flask_cors import CORS
from radius import *
from bts import *
import pandas as pd
import openpyxl
import json



app = Flask(__name__)
CORS(app)
#-----------------RADIUS------------------------------#
@app.route('/radius/users/createuser', methods = ['POST'])
def CreateUser():
    username = request.json['username']
    profile = request.json['profile']

    radius = RadiusServer()
    check_username = radius.FindRadiusUsers(username)
    if check_username ==True:
        return ('Existe')
    else:
        radius.CreateRadiusUser(username)
        radius.UpdateRadiusUser(username, profile)
        return('Exito')
    return ('ok')

@app.route('/radius/users/validar/<username>', methods = ['GET'])
def ValUser(username):
    radius = RadiusServer()
    check_username = radius.FindRadiusUsers(username)

    if check_username ==True:
        return ({"message":"True"})
    else:
        return ({"message":"False"})
    

@app.route('/radius/users/updateuser', methods = ['PUT'])
def UpgradeUser():
    
    username = request.json['username']
    profile = request.json['profile']
    radius = RadiusServer()
    
    check_username = radius.FindRadiusUsers(username)
    print (check_username)
    if check_username ==True:
        radius = RadiusServer()
        radius.UpdateRadiusUser(username, profile)
        return ('True')
    else:
        return ('El usuario no existe ')
    return ({"message":"Modificado"})

@app.route('/radius/users/edituser', methods = ['POST'])
def editUser():
    olduser = request.json['olduser']
    newuser = request.json['newuser']
    print(olduser, newuser)
    radius = RadiusServer()
    radius.EditRadiusUser(olduser, newuser)
    return ({"message":"Modificado"})

@app.route('/radius/users/finduser/<user>', methods = ['GET', 'POST'])
def FindUser(user):
    radius = RadiusServer()
    data = radius.FindRadiusUser(user)


    datos ={'id':data['id'],
        'username':data['username'],
        'profile':data['actual-profile']}
    
    return (datos)

@app.route('/radius/users/getusers',methods = ['GET','POST'])
def GetUser():
    radius = RadiusServer()
    data = radius.GetAllRadiusUsers()
    db = client.mikrotik_db
    datos = []
    for doc in data:
        datos.append({
            'id': doc['id'],
            'username': doc['username'],
            'profile': doc['actual-profile']
        })
    db.usuarios.insert_many(data)
    test = []
    for item in db.usuarios.find():
        test.append({
            'id': item['id'],
            'username':item['username'],
            'profile': item['actual-profile'],
        })

    return (jsonify(datos))

@app.route('/radius/users/deleteuser/<user>', methods = ['DELETE'])
def DeleteUser(user):
    radius = RadiusServer()
    check_username = radius.FindRadiusUsers(user)
    if check_username ==True:
        radius.DeleteRadiusUser(user)
        return('Usuario Borrado Con Exito')
    else:
        return ('Usuario no encontrado')
    return None

@app.route('/excel', methods = ['POST'])
def ExcelDoc():
    files = request.json['file']
    df_json = pd.read_json(files)
    df_json.to_excel('morosos.xlsx')

    toconvert = pd.read_excel('morosos.xlsx')

    listado = toconvert['Username'].values

    df = pd.DataFrame(listado, columns = ['Username'])
    #ELIMINA LOS VALORES NULOS
    test = df.dropna()
    #EXPORTA LA INFORMACION A EXCEL
    test.to_excel('morosos1.xlsx', sheet_name='morosos')

    #AGREGA EL ARCHIVO MODIFICACO
    archivo_excel = pd.read_excel('morosos1.xlsx')
    #AGREGA LOS DATOS DE LA COLUMNA RADIUS USER A UNA VARIABLE
    lista = archivo_excel['Username'].values
    #CONVIERTE LOS DATOS A UNA LISTA
    users_list = lista.tolist()
    #INICIA LA CONEXION CON EL SERVIDOR RADIUS
    print (users_list)
    radius = RadiusServer()
 
    for users in users_list:
        radius.UpdateRadiusUser(users, 'Morosos')

    return ({"message":"True"})
#--------------------ACCESS POINT-------------------------#
def ApData(valor: Any):
        apData = [
            {'codigo':'02.01', 'ip':'192.168.7.2'},{'codigo':'02.02', 'ip':'192.168.7.3'},{'codigo':'02.03', 'ip':'192.168.7.4'},
            {'codigo':'04.01', 'ip':'10.10.3.38'},{'codigo':'04.02', 'ip':'10.10.3.36'},{'codigo':'04.03', 'ip':'10.10.3.40'},
            {'codigo':'02.04', 'ip':'192.168.7.5'},{'codigo':'02.06', 'ip':'192.168.7.7'},{'codigo':'03.01', 'ip':'192.168.7.12'},
            {'codigo':'05.01', 'ip':'10.10.3.2'},{'codigo':'05.02', 'ip':'10.10.3.74'},{'codigo':'05.03', 'ip':'10.10.3.90'},
            {'codigo':'05.04', 'ip':'10.10.3.9'},{'codigo':'05.06', 'ip':'10.10.3.3'},{'codigo':'05.05', 'ip':'10.10.3.66'},{'codigo':'05.07', 'ip':'192.168.88.58'},
            {'codigo':'05.08', 'ip':'192.168.88.44'},{'codigo':'05.09', 'ip':'10.10.3.82'},{'codigo':'05.10', 'ip':'10.10.3.5'},
            {'codigo':'05.11', 'ip':'10.10.3.7'},{'codigo':'06.02', 'ip':'10.10.16.3'},{'codigo':'07.01', 'ip':'192.168.9.2'},
            {'codigo':'07.02', 'ip':'192.168.9.3'},{'codigo':'07.03', 'ip':'192.168.9.4'},{'codigo':'07.04', 'ip':'192.168.9.5'},
            {'codigo':'09.01', 'ip':'10.10.8.4'},{'codigo':'09.02', 'ip':'10.10.8.5'},{'codigo':'09.03', 'ip':'10.10.8.6'},
            {'codigo':'11.01', 'ip':'10.10.9.2'},{'codigo':'11.02', 'ip':'10.10.9.10'},{'codigo':'11.03', 'ip':'10.10.9.18'},
            {'codigo':'11.04', 'ip':'10.10.9.26'},{'codigo':'12.01', 'ip':'10.10.2.2'},{'codigo':'12.02', 'ip':'10.10.2.10'},
            {'codigo':'12.03', 'ip':'10.10.2.5'},{'codigo':'12.04', 'ip':'10.10.2.6'},{'codigo':'12.05', 'ip':'10.10.2.18'},
            {'codigo':'12.06', 'ip':'10.10.2.26'},{'codigo':'13.01', 'ip':'10.10.11.2'},{'codigo':'13.02', 'ip':'10.10.11.3'},
            {'codigo':'13.03', 'ip':'10.10.11.4'},{'codigo':'14.01', 'ip':'10.10.7.18'},{'codigo':'14.02', 'ip':'10.10.7.10'},
            {'codigo':'14.03', 'ip':'10.10.7.2'},{'codigo':'14.04', 'ip':'10.10.7.34'},{'codigo':'14.05', 'ip':'10.10.9.36'},
            {'codigo':'14.06', 'ip':'10.10.9.37'},{'codigo':'15.01', 'ip':'10.10.15.2'},{'codigo':'15.02', 'ip':'10.10.15.10'},
            {'codigo':'15.03', 'ip':'10.10.15.18'},{'codigo':'15.04', 'ip':'10.10.15.26'},{'codigo':'15.05', 'ip':'10.10.15.42'}
            ]

        for c in apData:
            if c['codigo'] == valor:
                return c
        return None

#--------------------BTS-------------------#
#Spammer
@app.route('/bts/spam', methods =['GET'])
def Spammer():
    ip = request.json['ip']
    user = request.json['user']
    pw = request.json['pw']

    bts = Bts(ip,user,pw)
    data = bts.getAddress_List()

    addressOnSpam = []
    for items in data:
        if items['list'] == 'Spammer':
            addressOnSpam.append(items['address'])
    active_users = bts.getActiveUsers()
    usersOnSpam = []

    for x in active_users:
        for c in addressOnSpam:
            if x['address'] == c:
                usersOnSpam.append({
                    'name':x['name'],
                    'address':x['address'],
                    'id':x['id']
                })
                
    return (jsonify(usersOnSpam))


#Morosos
@app.route('/bts/mora', methods = ['GET'])
def Morosos():
    ip = request.json['ip']
    user = request.json['user']
    pw = request.json['pw']

    bts = Bts(ip,user,pw)
    data = bts.getAddress_List()

    addressOnMora = []
    time = []
    for items in data:
        if items['list'] == 'Morosos':
            addressOnMora.append({'address':items['address'],
            'creation-time':items['creation-time']})




    active_users = bts.getActiveUsers()
    usersOnMora = []
    print(time)

    for x in active_users:
        for c in addressOnMora:
            if x['address'] == c['address']:
                usersOnMora.append({
                    'name':x['name'],
                    'address':x['address'],
                    'id':x['id'],
                    'creation-time':c['creation-time']
                })

    return (jsonify(usersOnMora))

@app.route('/bts/activeusers', methods = ['GET'])
def activeUsers():
    bts200 = Bts('10.99.99.2','redplanet01','****10596853$$$$')
    bts220 = Bts('10.99.99.3','redplanet01','****10596853$$$$')
    bts230 = Bts('10.99.99.8','redplanet01','****10596853$$$$')
    btsMoron = Bts('10.99.99.13', 'redplanet','****10596853')
    btsTabuyo = Bts('10.99.99.12', 'redplanet','****10596853')
    btsCalera = Bts('10.99.99.18', 'redplanet','****10596853')
    btsBlandon = Bts('10.99.99.13', 'redplanet01','****10596853')
    btsGuamal = Bts('10.99.99.6', 'redplanet','****10596853')
    btsIberia = Bts('10.99.99.5', 'redplanet','****10596853')
    olt_200 = bts200.ActiveUsers()
    olt_220 = bts220.ActiveUsers()
    olt_230 = bts230.ActiveUsers()

    return jsonify(len(olt_200 + olt_220 + olt_230))
    








if __name__ == "__main__":
    app.run(debug=True)