from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html',{'data': 'Django data'})

def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split(' ')
    wordDict = {}
    for word in wordList:
        if word in wordDict:
            # inc
            wordDict[word] += 1
        else:
            # add to dict
            wordDict[word] = 1

        sortedWords = sorted(wordDict.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'wordcount': len(wordList), 'worddict': sortedWords[0:3]})


def aboutPage(request):
    return render(request, 'about.html')


