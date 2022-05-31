#  This is created by me 
from django.http import HttpResponse
from django.shortcuts import render, redirect
import re

def index(request):
    return render(request,'home2.html',{'flag' : 0})


def output(request):
    myText = request.POST.get('text','default')
    removePunc = request.POST.get('removePunc','off')
    caps = request.POST.get('caps','off')
    spaceRemv = request.POST.get('spaceRemv','off')

    if(removePunc != "on" and spaceRemv!="on" and caps!="on"):
        return HttpResponse("OOPs ! Please select a operation")

    op = []

    operation = ""
    if(removePunc == 'on') :
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in myText:
            if char not in punctuations:
                analyzed = analyzed + char
        myText = analyzed
        op.append("Remove Punctuations")

    if(caps == 'on') :
        analyzed = ""
        for char in myText:
            analyzed = analyzed + char.upper()
        myText = analyzed
        op.append("Capitalize")
        # params = {'analyzed_text' : myText, 'operation' : 'caps'}

    if(spaceRemv == 'on') :
        analyzed = ""
        length = len(myText)
        for i in range(length-1):
            if not(myText[i]==" " and myText[i+1] == " "):
                analyzed = analyzed + myText[i]
        op.append("Removed Extra spaces")
        myText = analyzed
    # return render(request,'output.html',params)
    flag = 1
    params = {'analyzed_text' : myText, 'operation' : operation, 'op' : op, 'flag' : flag}
    return render(request,'output.html',params)
    # return redirect('https://www.google.com/')
