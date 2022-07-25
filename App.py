from User import User
from UserRepository import UserRepository
def app():
    userRepository=UserRepository()
    while True:
        print("Menü".center(50,"*"))
        secim=int(input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçiminiz:"))

        if secim==5:
            break
        else:
            if secim==1:
                username=input("username:")
                password=input("password:")
                email=input("email")
                newUser=User(username,password,email)
                userRepository.register(newUser)
            elif secim==2:
                if userRepository.isLoggedIn:
                    print("aynı anda iki kullanıcı giriş yapamaz")
                else:       
                    username=input("username:")
                    password=input("password:")
                    userRepository.login(username,password)
            elif secim==3:
                userRepository.logout(userRepository.currentUser)
            elif secim==4:
                userRepository.identity()
app()