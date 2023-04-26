import os
import requests

class Firebase:
    def __init__(self, projectid, authtoken, domain=False):
        self.base_url = "https://{}-default-rtdb.firebaseio.com".format(projectid)
        self.apikey = authtoken
        self.auth_token = "?auth="+ authtoken
        self.domain = domain

    def push(self, endpoint, data):
        if endpoint[0] == "/":
            if endpoint[-5:-1] == ".jso":
                return requests.post(self.base_url+endpoint+self.auth_token, json=data).json()
            else:
                return requests.post(self.base_url+endpoint+".json"+self.auth_token, json=data).json()
        else:
            if endpoint[-5:-1] == ".jso":
                return requests.post(self.base_url+"/"+endpoint+self.auth_token, json=data).json()
            else:
                return requests.post(self.base_url+"/"+endpoint+".json"+self.auth_token, json=data).json()
                
    
    def put(self, endpoint, data):
        if endpoint[0] == "/":
            if endpoint[-5:-1] == ".jso":
                return requests.put(self.base_url+endpoint+self.auth_token, json=data).json()
            else:
                return requests.put(self.base_url+endpoint+".json"+self.auth_token, json=data).json()
        else:
            if endpoint[-5:-1] == ".jso":
                return requests.put(self.base_url+"/"+endpoint+self.auth_token, json=data).json()
            else:
                return requests.put(self.base_url+"/"+endpoint+".json"+self.auth_token, json=data).json()
    
    def update(self, endpoint, data):
        if endpoint[0] == "/":
            if endpoint[-5:-1] == ".jso":
                return requests.patch(self.base_url+endpoint+self.auth_token, json=data).json()
            else:
                return requests.patch(self.base_url+endpoint+".json"+self.auth_token, json=data).json()
        else:
            if endpoint[-5:-1] == ".jso":
                return requests.patch(self.base_url+"/"+endpoint+self.auth_token, json=data).json()
            else:
                return requests.patch(self.base_url+"/"+endpoint+".json"+self.auth_token, json=data).json()

    
    def delete(self, endpoint):
        if endpoint[0] == "/":
            if endpoint[-5:-1] == ".jso":
                return requests.delete(self.base_url+endpoint+self.auth_token).json()
            else:
                return requests.delete(self.base_url+endpoint+".json"+self.auth_token).json()
        else:
            if endpoint[-5:-1] == ".jso":
                return requests.delete(self.base_url+"/"+endpoint+self.auth_token).json()
            else:
                return requests.delete(self.base_url+"/"+endpoint+".json"+self.auth_token).json()

    def get(self, endpoint):
        if endpoint[0] == "/":
            if endpoint[-5:-1] == ".jso":
                return requests.get(self.base_url+endpoint+self.auth_token).json()
            else:
                return requests.get(self.base_url+endpoint+".json"+self.auth_token).json()
        else:
            if endpoint[-5:-1] == ".jso":
                return requests.get(self.base_url+"/"+endpoint+self.auth_token).json()
            else:
                return requests.get(self.base_url+"/"+endpoint+".json"+self.auth_token).json()
