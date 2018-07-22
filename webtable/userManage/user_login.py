from webtable.models import User

from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        print('User', username, 'loging start')

        all_users = User.objects.all()
        for user in all_users:
            print('Debug all users in user login function:', user.Username)

        print('Debug user info before login:', username, passwd)
#        res = User.objects.filter(Username=username, Password=make_password(passwd))
        res = User.objects.filter(Username=username, Password=passwd)
        if res:
            for u in res:
                print(u.Username, u.LoginStatus, u.Password)
                if not u.LoginStatus:
            #print('check for user result:', res)
        #if res:
                    User.objects.update(LoginStatus=True)
                else:
                    print('User', u.Username, 'login status is already True')

            user = User.objects.filter(Username=username, LoginStatus=True)
            for u in user:
                print(u.Username, u.LoginStatus)
                if u.LoginStatus:
                    return u.Username
                else:
                    print('User login status is False')
                    return False
        else:
            print('Wrong username or password!', username, passwd)
    else:
        print('request method is not POST')
        return False

