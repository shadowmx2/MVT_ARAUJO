from django.shortcuts import render
from django.http import HttpRequest
from MVT_APP.models import Familia
import datetime

def mi_familia(request):
    fam = Familia.objects.all()

    return render(request, 'familiares.html', {'familia':fam})    