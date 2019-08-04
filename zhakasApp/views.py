from django.shortcuts import render
from .models import Profile,Community

def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        pass
    else:
        return render(request,'contact.html')

def about(request):
    profiles = Profile.objects.all()
    return render(request,'about.html',{'profiles':profiles})

def community(request):
    persons = Community.objects.all()
    flags = [True if i%2==0 else False for i in range(len(persons))]
    persons = zip(flags,persons)
    return render(request,'community.html',{'persons':persons})
