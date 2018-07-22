from webtable.models import User
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
import time
import datetime
from django.http import HttpResponseRedirect


def user_registry(request):
    userinfo = []

    #User.objects.all().delete()

    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        passwd_again = request.POST.get("passwd_again")
        email = request.POST.get("email")
        print('debug user info in user registery function:', username, email)

        if passwd == passwd_again:
            tm = datetime.datetime.now()
            logtime = tm.strftime("%Y-%m-%d %H:%M:%S")
#            sql = User(Username=username, Password=make_password(passwd), Email=email, LoginStatus=False, LoginTime=logtime)
            sql = User(Username=username, Password=passwd, Email=email, LoginStatus=False, LoginTime=logtime)
            sql.save()

            #users = User.objects.all()
            users = User.objects.filter(Username=username)
            for user in users:
                print('debug user:', user.Username)

                if user:
                #return HttpResponseRedirect("../../templates/login/login.html")
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False



if __name__ == '__main__':
    user_registry(request)
