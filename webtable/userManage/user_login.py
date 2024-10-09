import json

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from webtable.models import User

def user_login(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    username = data.get("username")
    passwd = data.get("password")
    print('User', username, 'loging start')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Wrong username'}, status=400)

    if check_password(passwd, user.password):
        if not user.login_status:
            user.login_status = True
            user.save()
        return JsonResponse({'username': user.username})
    else:
        return JsonResponse({'error': 'Wrong username or password'}, status=400)