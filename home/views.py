from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    User = 'admin'
    Pass = 'admin'


    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password_name')
        print("Username:", username)
        print("Password:", password)


    return render(request, 'home/home.html')