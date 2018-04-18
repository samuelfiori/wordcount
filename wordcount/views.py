from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html")
def count(request):
    textfeld = request.GET['Textfeld']
    wortliste = textfeld.split()
    h = max(wortliste)
    hanzahl = wortliste.count(h)
    wortdict = {}
    for wort in wortliste:
        if wort in wortdict:
            wortdict[wort] += 1
        else:
            wortdict[wort] = 1
    sortiert = sorted(wortdict.items(), key=operator.itemgetter(1), reverse=True)
    return render(
        request,
        "count.html",
        {'textfeld': textfeld, 'count': len(wortliste), 'most': h, 'hmost': hanzahl, 'dict': sortiert}
    )

def kontakt(request):
    return render(request, "kontakt.html")