from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login


def dashboard(request):
    return render(request, 'home/dashboard.html')


# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password_name')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or do further processing
            return redirect('dashboard')
        else:
            # Authentication failed, handle the error
            return render(request, 'home/login.html', {'error': 'Invalid credentials'})

    return render(request, 'home/login.html')
