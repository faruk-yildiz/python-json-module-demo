from User import User
import json
import os

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)
                    newUser=User(username=user['username'],password=user['password'],email=user['email'])
                    self.users.append(newUser)
    def register(self,user:User):
        self.users.append(user) 
        self.saveToFile()
        print("kullanici olusturuldu ")
    def login(self,username,password):
        for user in self.users:
            if username==user.username and password==user.password:
                self.isLoggedIn=True
                self.currentUser=user
                print("login")
                break   
    def logout(self):
        if self.isLoggedIn:
            self.isLoggedIn=False
            self.currentUser={}
            print("cikis yapildi")
        else:
            print("henüz giriş yapılmadı")
    def identity(self):
        if self.isLoggedIn:
            print(f"username {self.currentUser.username}")
        else:
            print("giriş yapılmadı") 
    def saveToFile(self):
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("users.json","w") as file:
            json.dump(list,file)

