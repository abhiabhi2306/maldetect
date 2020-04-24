from django.shortcuts import render
from django.http import HttpResponse
from .forms import MalUrlForm
import urllib.request as urllib
import os
import re
import json
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
        return True
    except ValidationError:
        return False
        
        

def handler500(request, *args, **argv):
    response = render_to_response('urlerror.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def malurl_form(request):
    #header = {'API-Key':"58e461c6-fb17-4f5e-ba91-26cd32710bd9"}
    #apiurl = "https://urlscan.io/api/v1/scan/"
    if request.method == 'POST':
        form = MalUrlForm(request.POST)

        if form.is_valid():
            geturl = request.POST.get("url", "")
            if is_valid_url(geturl)==False:
               return render(request, 'urlerror.html')
            #cmd = "curl -s -H 'API-Key: 58e461c6-fb17-4f5e-ba91-26cd32710bd9'  -X POST --data \"url="+geturl+"\""+" https://urlscan.io/api/v1/scan/"
            cmd = "curl --request GET --url 'https://www.virustotal.com/vtapi/v2/url/report?apikey=04f6969b2a33d59dab83d4c8283f00aeb0a7e17b1823c61012bfe87c927ba07b&resource="+geturl+"'"
            #print(cmd)
            #resp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            resp = os.popen(cmd)
            output = resp.read()
            imprint = json.loads(output)['positives']
            print(imprint)
            if imprint==1:
               result="The site may be malicious, "+str(imprint)+ " of our databases has marked it as malicious"
            elif imprint>1:
               result="The site is malicious, "+str(imprint)+" of our databases has marked it as malicious"
            else:
               result="The site seems to be safe according to our databases"
            print(result)
            '''req = {"url":geturl}
            response = request.POST("https://urlscan.io/api/v1/scan/",data=req,headers=header)
            if response.status_code == 200:
                respcontent = response.content
            else:
                respcontent = "An error occured"
            print (url)
            form.save()
            r = Request(url='http://www.mysite.com')
            r.add_header('User-Agent', 'awesome fetcher')
            r.add_data(urllib.urlencode({'foo': 'bar'})
            resp = urllib.urlopen(r)'''
            return render(request, 'result.html', {'result': result})
    else:
        form = MalUrlForm()
    return render(request, 'index.html', {'form': form})
