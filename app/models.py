from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=60)
    curso = models.CharField(max_length=40)
    rgm = models.IntegerField(unique=True)
    semestre = models.IntegerField()

    def __str__(self):
        return self.nome