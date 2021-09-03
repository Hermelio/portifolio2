from  django import forms
from  django.forms import  ModelForm, fields, Textarea
from .models import Contato
from  . import models





class QuestionForm(ModelForm):
    class Meta:
        model = models.Contato
        fields = ["email", "text", "nome"]