import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from .models import links

# Create your views here.
def home(request):
    if request.method=='POST':
        links.objects.all().delete()
        link_new = request.POST.get('page','')
        urls = requests.get(link_new)
        beautysoup = BeautifulSoup(urls.text,'html.parser')

        for link in beautysoup.find_all('a'):
            li_address = link.get('href')
            li_name = link.get_text()
            links.objects.create(address_link=li_address, name_link=li_name)
        return redirect('/')
    else:
            data_values = links.objects.all()

    return render(request,'home.html',{'data_values':data_values})
