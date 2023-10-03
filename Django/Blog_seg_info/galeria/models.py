from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    legenda = models.CharField(max_length=150,null=False,blank=False)
    descricao = models.TextField(null=False,blank=False)
    link = models.CharField(max_length=150, null = True)
    foto = models.ImageField(upload_to= "fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


