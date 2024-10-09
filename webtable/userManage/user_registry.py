import json
from webtable.models import User
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
import datetime
from django.http import JsonResponse


def user_registry(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    username = data.get("username")
    passwd = data.get("password")
    passwd_again = data.get("passwd_again")
    email = data.get("email")
    print('debug user info in user register function:', request.method, username, passwd, passwd_again, email)

    if passwd == passwd_again:
        tm = datetime.datetime.now()
        logtime = tm.strftime("%Y-%m-%d %H:%M:%S")
        sql = User(username=username, password=make_password(passwd), email=email, login_status=False,
                   login_time=logtime)
        sql.save()

        users = User.objects.filter(username=username)
        for user in users:
            print('debug user:', user.username)
            if user:
                return JsonResponse({'success': 'User registered successfully'})
        return JsonResponse({'error': 'User registration failed'}, status=400)
    else:
        return JsonResponse({'error': 'Passwords do not match'}, status=400)