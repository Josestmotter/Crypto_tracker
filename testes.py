import requests 
def preco_crypto(moeda):
    url = f"https://api.coinbase.com/v2/prices/{moeda}-USD/spot"
    dados = requests.get(url)
    resposta = dados.json()
    preco = resposta["data"]["amount"]
    return render(request, "home.html", preco)
x = preco_crypto("BTC")
print(x)