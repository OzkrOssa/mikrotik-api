import routeros_api

class AccessPoint:

    def __init__(self):
        self.api = routeros_api.RouterOsApiPool('192.168.7.2','redplanet', '$$$$red1059', plaintext_login=True).get_api()

    def AccessList(self, mac, name):
        self.api.get_binary_resource('/interface/wireless').call('access-list/add',{'mac-address':mac,'comment':name})

    def Regitration():
        data = self.api.get_resource('/interface/wireless/registration-table').get()
        return data