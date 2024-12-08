from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
  msg = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Página Inicial</title>
    </head>
    <body>
      <h1>Bem-vindo(a)!</h1>
      <a href="/index/">Formulário para fazer o cálculo</a><br>
      <a href="/autor/">Sobre o autor</a>
    </body>
    </html>
  """
  return HttpResponse(msg)

def index(request):
  msg = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Formulário</title>
    </head>
    <body>
        <h1>Formulário do cálculo</h1>
        <p>Soma de dois números</p>
        <form action="/calcular/" method="post">
            <label for="valor1">Valor 1:</label>
            <input type="number" id="valor1" name="valor1" required>
            <label for="valor2">Valor 2:</label>
            <input type="number" id="valor2" name="valor2" required>
            <button type="submit">Calcular</button>
        </form>
    </body>
    </html>
  """
  return HttpResponse(msg)

@csrf_exempt
def calcular(request):
  if request.method == 'POST':
      valor1 = int(request.POST.get('valor1'))
      valor2 = int(request.POST.get('valor2'))
      resultado = valor1 + valor2
      msg = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Resultado</title>
        </head>
        <body>
            <h1>Resultado</h1>
            <p>A soma de {valor1} e {valor2} é igual a {resultado}.</p>
            <a href="/index/">Voltar para o formulário</a>
        </body>
        </html>
      """
      return HttpResponse(msg)

def autor(request):
  msg = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sobre o Autor</title>
    </head>
    <body>
        <h1>Sobre o Autor</h1>
        <p>Nome: Enaira</p>
        <p>Técnico em Informática para Internet, IFCE, 2024<p>
        <a href="/index/">Voltar para o formulário</a>
    </body>
    </html>
  """
  return HttpResponse(msg)


      