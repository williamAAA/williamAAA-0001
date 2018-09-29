from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, 'homepage.html')
#def homepage(request):
    #return HttpResponse("django!")
def here(request):
    return HttpResponse("<h1>Mom I am here!</h1>")
def count(request):
    fulltext=request.GET['fulltext']
    wordlist= fulltext.split()
    dicA={}
    for i in range(0,len(wordlist)):
        if wordlist[i] not in dicA:
            dicA[wordlist[i]]=1
        else:
            dicA[wordlist[i]]+=1
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),"dicA":dicA})

