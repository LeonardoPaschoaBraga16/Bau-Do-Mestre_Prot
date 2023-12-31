from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Campanha, Perfil
from .forms import CampanhaForm, PerfilForm
from django.db.models import Q
from functools import wraps
from random import randint
import os
import shutil


# Decorator manual feito para impedir que não mestres entrem no link pela url
def jogadores_permitidos(required_types):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            perfil = Perfil.objects.get(nomePerfil=request.user)
            if perfil.tipo_player in required_types:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('buscarmesa')
        return _wrapped_view
    return decorator

# Tela de 404
def handler404(request, exception):
    aleatorio = randint(1, 6)
    return render(request, 'principal/404.html', {'aleatorio': aleatorio})

# view da home
def index(request):
    return render(request, 'principal/home.html')

# view do mural não logado
def mural(request):
    campanhas = Campanha.objects.all()
    return render(request, 'principal/mural.html', {'campanhas': campanhas})

# views do mural logado + buscar as mesas
@login_required
def buscarmesa(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
    sistema_busca = request.GET.get('q')
    sistema_filtro = request.GET.get('sistema')
    ambiente_filtro = request.GET.get('ambiente')
    genero_filtro = request.GET.get('genero')
    campanhas = Campanha.objects.all()


    if sistema_busca:
        campanhas = campanhas.filter(
            Q(nomeCampanha__icontains=sistema_busca)
        )
    if sistema_filtro:
        campanhas = campanhas.filter(
            Q(sistemaCampanha__icontains=sistema_filtro)
        )
    if ambiente_filtro:
        campanhas = campanhas.filter(
            Q(ambienteCampanha__icontains=ambiente_filtro)
        )
    if genero_filtro:
        campanhas = campanhas.filter(
            Q(generoRPG__icontains=genero_filtro)
        )

    return render(request, 'principal/muralLogado.html', {'campanhas': campanhas, 'perfil': perfil})


# view da busca de usuários
@login_required
def search_user(request):
    conta_busca = request.GET.get('q')
    users = []
    if conta_busca:
        users = Perfil.objects.filter(
            Q(nomePerfil__username__icontains=conta_busca)
        )
    return render(request, 'principal/buscaUser.html', {'users': users, 'busca_realizada': bool(conta_busca)})


# view do perfil com link slug dos usuários
@login_required
def exibir_perfil(request, perfil_slug):
    perfil = get_object_or_404(Perfil, slug=perfil_slug)
    return render(request, 'principal/exibir_perfil.html', {'perfil': perfil})


# view da criação de campanhas que também é protegida por um decorator que só permite a entrada de "Mestre" e "Ambos"
@login_required
@jogadores_permitidos(["Mestre", "Ambos"])
def criarCampanhas(request):
    if request.method == 'POST':
        form = CampanhaForm(request.POST, request.FILES)
        if form.is_valid():
            campanha = form.save(commit=False)
            perfil_mestre = get_object_or_404(Perfil, nomePerfil=request.user)
            campanha.nomeMestre = perfil_mestre
            campanha.save()
            return redirect('buscarmesa')
    else:
        form = CampanhaForm()

    return render(request, 'principal/criarMesas.html', {'form': form})


# view da conta do usuário logado
@login_required
def usuario(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
    return render(request, 'principal/user.html', {'perfil': perfil})


# view da edição de conta do usuário
@login_required
def editarconta(request):
    perfil, created = Perfil.objects.update_or_create(nomePerfil=request.user)

    if request.method == 'POST':
        formPerfil = PerfilForm(request.POST, request.FILES, instance=perfil)
        if formPerfil.is_valid():
            if 'fotoConta' in request.FILES:
                nova_foto = formPerfil.cleaned_data.get('fotoConta', None)
                if nova_foto:
                    nome_usuario = perfil.nomePerfil.username
                    caminho_destino = f'static/img/fotoUser/{nome_usuario}.png'

                    try:
                        with open(caminho_destino, 'wb') as destino:
                            for chunk in nova_foto.chunks():
                                destino.write(chunk)
                    except Exception as e:
                        print(f"Erro ao salvar a nova foto: {e}")
                    else:
                        perfil.fotoConta = caminho_destino

                    formPerfil.save()
                    return redirect('usuario')

    else:
        formPerfil = PerfilForm(instance=perfil)

    return render(request, 'principal/editarPerfil.html', {'formPerfil': formPerfil})
