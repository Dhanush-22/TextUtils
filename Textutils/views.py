#  This is created by me 
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request,'home2.html')


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

    params = {'analyzed_text' : myText, 'operation' : operation, 'op' : op}

    return render(request,'output.html',params)




def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover','off')





    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
