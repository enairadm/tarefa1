from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from .models import Aluno, Professor
from .serializers import AlunoSerializer, ProfessorSerializer

class AlunoViewSet(viewsets.ModelViewSet):
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
  queryset = Professor.objects.all()
  serializer_class = ProfessorSerializer

def home(request):
  return render(request, 'home.html')

def index(request):
  return render(request, 'index.html')

@csrf_exempt
def calcular(request):
  if request.method == 'POST':
      valor1 = int(request.POST.get('valor1'))
      valor2 = int(request.POST.get('valor2'))
      resultado = valor1 + valor2
      return render(request, 'calcular.html', {'resultado': resultado, 'valor1': valor1, 'valor2': valor2})

def autor(request):
  return render(request, 'autor.html')



      