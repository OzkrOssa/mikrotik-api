import routeros_api
from typing import Any


class Bts:

    
    #Constructor
    def __init__(self,ip_bts,user_bts,pw_bts):
        self.ip_bts = ip_bts
        self.user_bts = user_bts
        self.pw_bts = pw_bts
        self.api = routeros_api.RouterOsApiPool(self.ip_bts, self.user_bts, self.pw_bts, plaintext_login=True).get_api()


    #Funcionalidad interfaz mikrotik

    def GetMonitorTraffic (self):
        while True :
            monitor_traffic = self.api.get_binary_resource('/interface').call('monitor-traffic',{'interface':b'ether1','once':b''})
            data_rx = monitor_traffic[0]['rx-bits-per-second']
            data_tx = monitor_traffic[0]['tx-bits-per-second']
            self.rx = data_rx.decode()
            self.tx = data_tx.decode()

    def ipPing(self, ip, count):
        return self.api.get_binary_resource('/').call('ping', { 'address': ip.encode(), 'count': count.encode() })
        
    def getPppActiveUsers(self):
            return self.api.get_resource('/ppp/active').get()

    def getSecretUsers(self):
        return self.api.get_resource('/ppp/secret').get()


    def getLog(self):
        log = self.api.get_resource('/log').get()
        data = []
        for x in log:
            if x['topics']=='pppoe,ppp,error':
                data.append({
                    'time':x['time'],
                    'message': x['message']
                })
        return data

    def getAddressList (self):
        return self.api.get_resource('/ip/firewall/address-list').get()

    def getInterfaces (self):
        return self.api.get_resource('/interface').get()
    
    def setProfile(self, profile, pppoe):

        try:
            self.api.get_binary_resource('/ppp/secret').call('set',{'numbers':pppoe.encode(),'profile':profile.encode()})
            return True

        except:
            pass
    
    def removePppActiveUsers (self, pppoe):
        try:
            self.api.get_binary_resource('/ppp/active').call('remove',{'numbers':pppoe.encode()})

            return ({"message":"Usuario Borrado"})

        except:

            return ({"message":"Error"})

    def removePppActiveUsersWithId(self, id):
            return self.api.get_resource('/ppp/active').remove(id=id)

    def createSecretUser(self, pppoe):
        try:
            self.api.get_binary_resource('/ppp/secret').call('add',{'name':pppoe.encode(), 'password':b'redplanet', 'profile':b'default', 'service':b'pppoe'})
            return ({"message":"Usuario creado localmente con exito"})
        except:
            pass


    





    
