from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    return render(request, 'accounts/sign_up.html')


def sign_in(request):
    return render(request, 'accounts/sign_in.html')


def sign_out(request):
    return render(request, 'accounts/sign_out.html')


def reset(request):
    pass


def forgot(request):
    pass
