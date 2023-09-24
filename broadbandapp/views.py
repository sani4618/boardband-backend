from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# customerid:"",customerName:"",broadbandplan:"",mobileNo:"",subDate:"",NxtSubDate:"",amount:"",address:"",pincode:"",ntwid:""
           
@csrf_exempt
def NewRegsubscribers(request):
    if request.method=="POST":
        recieved_json_data=json.loads(request.body)
        getcustomerid=recieved_json_data["customerid"]
        getcustomerName=recieved_json_data["customerName"]
        getbroadbandplan=recieved_json_data["broadbandplan"]
        getMobileNum=recieved_json_data["mobileNo"]
        getSubscriptionDate=recieved_json_data["subDate"]
        getnxtsubdate=recieved_json_data["NxtSubDate"]
        getAmount=recieved_json_data["amount"]
        getAddress=recieved_json_data["address"]
        getPincode=recieved_json_data["pincode"]
        getntwId=recieved_json_data["ntwid"]
        data={"customerid":getcustomerid,"customerName":getcustomerName,"broadbandplan":getbroadbandplan,"mobileNo":getMobileNum,"subDate":getSubscriptionDate,"NxtSubDate":getnxtsubdate,"amount":getAmount,"address":getAddress,"pincode":getPincode,"ntwid":getntwId}
        print(data)
        return HttpResponse(json.dumps({"status":"Registered Successfully"}))
    else:
        return HttpResponse("Registerion failed")