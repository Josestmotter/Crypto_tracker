from django.shortcuts import render
from django.http import JsonResponse
from decimal import Decimal
import requests
from django.db.models.functions import TruncHour
from home.models import PrecoMoeda
from django.db.models import Max

def buscar_preco(moeda):
    url = f"https://api.coinbase.com/v2/prices/{moeda}-USD/spot"
    resposta = requests.get(url).json()
    preco = Decimal(resposta["data"]["amount"])
    return preco


def salvar_moeda(moeda, preco):
    ultimo = PrecoMoeda.objects.filter(moeda=moeda).order_by("-criado_em").first()

    if not ultimo or ultimo.preco != preco:
        PrecoMoeda.objects.create(moeda=moeda, preco=preco)


def home(request):
    return render(request, "home/home.html")


def preco(request):
    moeda = request.GET.get("moeda", "BTC").upper()

    if moeda not in ["BTC", "ETH", "SOL"]:
        return JsonResponse({"erro": "Moeda inválida"}, status=400)

    preco_atual = buscar_preco(moeda)
    salvar_moeda(moeda, preco_atual)

    return JsonResponse({
        "moeda": moeda,
        "preco": str(preco_atual)
    })




def historico(request):
    moeda = request.GET.get("moeda", "BTC").upper()

    horas = (
        PrecoMoeda.objects
        .filter(moeda=moeda)
        .annotate(hora=TruncHour("criado_em"))
        .values("hora")
        .annotate(ultimo_id=Max("id"))
        .order_by("hora")
    )

    ids = [item["ultimo_id"] for item in horas]

    registros = PrecoMoeda.objects.filter(id__in=ids).order_by("criado_em")

    labels = [item.criado_em.strftime("%d/%m %H:00") for item in registros]
    precos = [float(item.preco) for item in registros]

    return JsonResponse({
        "moeda": moeda,
        "labels": labels,
        "precos": precos
    })