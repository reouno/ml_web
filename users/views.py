from django.http import HttpResponse

from users.models import CustomUser


def index(request):
    return HttpResponse('こんにちは。')
