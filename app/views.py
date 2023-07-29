from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from app.models import Autores
from app.forms import AutoresForm
from django.db.models import Count
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def home(request):
    data = {}
    data['db'] = Autores.objects.all()
    all = Autores.objects.all()
    paginator = Paginator(all, 2)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    search = request.GET.get('search')
    if search:
        data['db'] = Autores.objects.filter(autor__icontains=search)
    else:
        data['db'] = Autores.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form']= AutoresForm()
    return render(request, 'form.html', data)

def create(request):
    form = AutoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Autores.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Autores.objects.get(pk=pk)
    data['form'] = AutoresForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data ={}
    data['db']=Autores.objects.get(pk=pk)
    form = AutoresForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save
        return redirect('home')

def delete(request, pk):
    db = Autores.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def relatorio_detalhado(request):
    # Query para contar o número de registros por combinação de país e estado
    dados_agrupados = Autores.objects.values('pais', 'estado').annotate(count=Count('id'))

    # Preparando os dados para o gráfico de barras
    labels = []
    data = []
    for dado in dados_agrupados:
        labels.append(f"{dado['pais']} - {dado['estado']}")
        data.append(dado['count'])

    return render(request, 'relatorio_detalhado.html', {
        'labels': labels,
        'data': data,
    })

def relatorio_por_data(request):
    # Recupere os dados do modelo
    dados = Autores.objects.all()

    # Preparando dados para o gráfico de linhas e pontos
    datas_inicio = [dado.data_inicio for dado in dados]
    datas_entrega = [dado.data_entrega for dado in dados]
    estados = [dado.estado for dado in dados]
    cidades = [dado.cidade for dado in dados]
    instituicoes = [dado.instituicao for dado in dados]

    # Criando o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(datas_inicio, label='Data Início', marker='o')
    plt.plot(datas_entrega, label='Data Entrega', marker='o')
    plt.xticks(rotation=45)
    plt.xlabel('Registros')
    plt.ylabel('Datas')
    plt.title('Historico de registros por data, estado e cidade')
    plt.legend()

    # Convertendo o gráfico para base64 para exibir no template
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    return render(request, 'relatorio_por_data.html', {'plot_data': plot_data})