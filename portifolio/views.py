from django.shortcuts import render
from . import models
from . import forms
from django.http import request, response
from .forms import QuestionForm
from django.shortcuts import redirect
# Create your views here.


def pagina_inicial(request):
    pagina = 'portifolio2/base.html'

    return render(request, pagina)


def contato(request):
    if request.method == "POST":
        print(request.POST["email"])

    return render(request, 'portifolio2/base.html')
