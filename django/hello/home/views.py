from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact  # This is your model
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact_view(request):  # ✅ rename this function
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact_entry = contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact_entry.save()
        messages.success(request,'Thank you for contact me...')
    return render(request, 'contact.html')
