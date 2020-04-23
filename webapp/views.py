from django.shortcuts import render
from django.http import HttpResponse
from .forms import MalUrlForm
from urllib import request


def malurl_form(request):
    header = {'API-Key':"58e461c6-fb17-4f5e-ba91-26cd32710bd9"}
    apiurl = "https://urlscan.io/api/v1/scan/"
    if request.method == 'POST':
        form = MalUrlForm(request.POST)

        if form.is_valid():
            '''geturl = request.POST.get("url", "")
            data = dict(url=geturl)

            response = request.POST.get("https://urlscan.io/api/v1/scan/",headers=header,data=data)
            if response.status_code == 200:
                respcontent = response.content
            else:
                respcontent = "An error occured"
            print (url)
            form.save()'''
            return render(request, 'result.html')
    else:
        form = MalUrlForm()
    return render(request, 'index.html', {'form': form})
