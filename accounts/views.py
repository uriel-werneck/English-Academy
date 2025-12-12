from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    if request.method == "POST":
        pass
    return render(request, 'accounts/login.html')