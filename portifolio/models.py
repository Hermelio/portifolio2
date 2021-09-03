from django.db import models

# Create your models here.


class Contato(models.Model):
    email = models.EmailField(max_length=200)
    nome = models.CharField(max_length=200)
    text = models.TextField(max_length=254)

    def __str__(self):
        return self.nome + self.text + self.email
    class  Meta:
        verbose_name_plural = 'Contato'