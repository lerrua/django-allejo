from django.shortcuts import render

from allejo.models import Championship


def home(request):
    championships = Championship.objects.all()
    return render(
        request, 'demo/index.html', {'championships': championships})
