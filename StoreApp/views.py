from django.shortcuts import render
from StoreApp.models import Departamento
from StoreApp.models import Produto
from StoreApp.forms import ContatoForm

# Create your views here.

def index(request):
    produtos_em_destaque = Produto.objects.filter(destaque = True)

    context = {
        'produtos' : produtos_em_destaque
    }

    return render(request, 'index.html', context)


def produto_lista(request):
    # buscando produtos no banco 
    produtos = Produto.objects.all()

    context = {
        'produtos' : produtos,
        'categoria' : 'Todos Produtos'
    }

    return render(request, 'produtos.html', context)

def produto_lista_por_id(request, id):
    # buscando produtos no banco filtrando por dpto
    produtos = Produto.objects.filter(departamento_id = id)
    # buscar departamento no banco 
    departamento = Departamento.objects.get(id = id)

    context = {
        'produtos' : produtos,
        'categoria' : departamento.nome
    }

    return render(request, 'produtos.html', context)


def produto_detalhe(request, id):
    produto = Produto.objects.get(id = id)
    produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento.id).exclude(id = id)[:4]


    context = {
        'produto' : produto,
        'produtos_relacionados' : produtos_relacionados
    }
    return render(request, 'produto_detalhes.html', context)

def institucional(request):
    return render(request, 'institucional.html')

def contato(request):
    formulario = ContatoForm()

    context = {
        'form_contato' : formulario
    }    
    
    return render(request, 'contato.html', context)