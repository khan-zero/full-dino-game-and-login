from django.shortcuts import render

def register(request):
    return render(request, 'register.html')
    
def registration_success(request):
    return render(request, 'registration_success.html')
