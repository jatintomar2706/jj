from django.shortcuts import render,HttpResponse,redirect
import ast
import json
from logogen import check
from Details import details
# Create your views here.
import requests
def view(request):
    if request.method=="POST":
            if request.GET.get('search') != "None":
                
                response=check(request.POST.get('search'))
                list=[]
                data_list = ast.literal_eval(response)

                list.append(data_list)
                print(list)
                return render(request , 'abc.html', context={'stock_names' : list , 'header' : "Search Results :"} )
    Symbols=["MSFT" , "NVDA" , "AMZN" , "META" , "LLY" , "TSLA" , "AVGM" ,"V" , "JPM" , "UNH"]
    with open('output.json' , "r") as json_file:
        new_data = json.load(json_file)
        print(type(new_data))
        print(new_data)


    
    return render(request , 'abc.html', context={'stock_names' : new_data , 'header' : "Top stocks :"} )


def det_func(request ,key):
    key_stock=key
    
    
    funda=["EBITDA","PERatio","PEGRatio","BookValue","DividendPerShare","DividendYield","EPS","RevenuePerShareTTM","ProfitMargin","OperatingMarginTTM","ReturnOnAssetsTTM","ReturnOnEquityTTM","RevenueTTM","GrossProfitTTM","DilutedEPSTTM","QuarterlyEarningsGrowthYOY","QuarterlyRevenueGrowthYOY"] 
    tech_num=[]
    tech_data=[]
    data1=eval(details(key_stock))
    print(type(data1))
   
    data = eval(details(key_stock))
    print(type(data))
    print(data)
    for key,value in data.items():
        if key in funda:
               if value=='None':
                    value=0
               data[key]=float(value)
               tech_num.append({key:value})
        else:
              tech_data.append({key:value})
    # print(tech_num)
    print("enter in detfun")
    print("this is --"+key)
    basic=check(key_stock)
    basic= ast.literal_eval(basic)
    print(basic)
    return render(request , "Details.html" , context={'data':data ,'tech_num' : tech_num ,'tech_data': tech_data, 'basic' : basic})


def login(request):
     return render(request,"Login.html")

def main(request):
     email=str(request.GET.get('email'))
     pswd=str(request.GET.get('password'))
     return redirect('/home')
    
