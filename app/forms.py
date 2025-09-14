from django import forms
from .models import Aluno, Professor

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'curso', 'rgm', 'semestre']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'formacao', 'especialidade', 'email']