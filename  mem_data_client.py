import requests
import base64

class Client():
    def __init__(self,host):
        self.host=host
    def shell(self,c):
        result=requests.post(self.host+'/?parameter='+base64.urlsafe_b64encode(c.encode()).decode() ).text
        return result
    def get(self,data):
        c="self.data={'data':%s}"%(data)
        result=requests.post(self.host+'/?parameter='+base64.urlsafe_b64encode(c.encode()).decode() ).text
        return result
