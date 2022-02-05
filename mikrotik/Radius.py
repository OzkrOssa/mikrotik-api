import routeros_api
from typing import Any


class RadiusServer:

    def __init__(self):

        self.api = routeros_api.RouterOsApiPool('10.99.99.4', 'redplanet', '****10596853',
                                                plaintext_login=True).get_api()
        self.list_user = self.api.get_resource('/tool/user-manager/user').get()

    def CreateRadiusUser(self, user_ppoe):

        self.api.get_binary_resource('/').call(
            'tool/user-manager/user/add',
            {'username': user_ppoe.encode(), 'password': b'redplanet', 'customer': b'REDPLANET', 'caller-id-bind-on-first-use':b'yes'})

    def DeleteRadiusUser(self, user_ppoe):

        self.api.get_binary_resource('/').call(
            'tool/user-manager/user/remove',
            {'numbers': user_ppoe.encode()})

    def UpdateRadiusUser(self, user, profile):
        #self.api.get_binary_resource('/').call(
            #'tool/user-manager/user/clear-profile',
            #{'numbers': user.encode()})

        self.api.get_binary_resource('/').call(
            'tool/user-manager/user/create-and-activate-profile',
            {'numbers': user.encode(), 'profile': profile.encode(), 'customer': b'REDPLANET'})

    def EditRadiusUser(self, user, username):
        self.api.get_binary_resource('/').call(
            'tool/user-manager/user/set',
            {'numbers': user.encode(), 'username':username.encode()})

    def FindRadiusUsers(self, valor: Any):
        for x in self.list_user:
            if x['username'] == valor:
                print ('Usuario Ya Existe')
                return True
        print ('Usuario Creado')
        return None

    def GetAllRadiusUsers(self):
        data = self.list_user
        return data
    
    def FindRadiusUser(self, valor: Any):
        for x in self.list_user:
            if x['username'] == valor:
                return x
        return None