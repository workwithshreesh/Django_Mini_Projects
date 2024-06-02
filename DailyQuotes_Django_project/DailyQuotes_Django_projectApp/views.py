from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
import datetime
# Create your views here.


def index(request):
    import requests

    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    
    
    cached_quote=cache.get('cached_quote')
    if cached_quote:
        today=datetime.date.today()
        if cached_quote['date']==today:
            return render(request,'index.html',cached_quote['data'])
    
    response = requests.get(api_url, headers={'X-Api-Key': ''})
    
    if response.status_code == requests.codes.ok:
        data=response.json()
        quotes=data[0]['quote']
        author=data[0]['author']
        category=data[0]['category']
        datas={
            'quotes':quotes,
            'author':author,
            'category':category,
        }
        cache.set('cached_quote',{'data':datas,'date':datetime.date.today()})
        return render(request,'index.html',datas)
    else:
        return HttpResponse("Error:", response.status_code, response.text)
    
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')