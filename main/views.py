from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth 
from . import forms
import json
from django.http import JsonResponse
import jmespath
# Create your views here.

# user function that helps to search the key in the json
def search_json(data,entered_key):    
    if entered_key in data:
        print("key is present")
        return True
    else:
        print("key is absent")
        print(f"Please enter from the below keys: \n{data.keys()} ")
        return False
# user function that retrieves the values using the key
def get_value(get_val):
    if get_val == True:
        return data[entered_key]


def gettoken(request,server):
    url = server+"api/gettoken"
    myobj = {'Username':'charles.mutinda@educationhorizons.com','Password':'ynKOGn^14Nik'
             }
    response = requests.post(url,data=myobj)
    if response.status_code !=200:
        print(response.status_code,'Access Error')
    else:
        print('Authorised')
    data= response.json()
    request.session['token'] =data['access_token']
    return data['access_token']

def main(request):
    server ="http://192.168.68.117:8080/"
    schoolID='Sandbox'
    request.session['schoolID'] = schoolID
    url = server+"api/v1/lookups/GetAlllookups/"+schoolID
    response=requests.get(url)
    print(url,response.status_code)
    token={}

    if response.status_code == 401:
        token=gettoken(request,server)
        print(token)
    else:
        print('We are okay')    
    
    context={}
    context['token']=token
    form= forms.ParentForm
    if request.method =='POST':  
        form= forms.ParentForm(request.POST)
        if form.is_valid():
            headers = {'Authorization': 'Bearer '+token,}
            url=server+'api/v1/admissions/GetAllContactBasicInfo/'+schoolID
            cdata= form.cleaned_data
            print(cdata)
            email=cdata['email'].lower()
            response = requests.get(url,headers=headers)
            data = response.json()
            # print(data)
            print(json.dumps(data, indent=4))
            contactid=jmespath.search("[].emailAddresses[?emailAddress=='"+email+"'].contactId[]|[0]",data)
            # contactid=jmespath.search("[].emailAddresses[].emailAddress[?contains(lower(@), lower('string_you_want_to_search')].contactId[]|[0]",data)
            url=server+'api/v1/admissions/GetAllContactBasicInfo/'+schoolID

            print(contactid)
            
            url=server+'api/v1/admissions/GetAllContactBasicInfo/'+schoolID
            
    context['form']= form
    return render(request,'main.html',context)
 

