import urllib.request
import requests
from datetime import datetime


def getProductInformations(productId: str):
    baseURL = 'https://cosmetics2.vtexcommercestable.com.br/api/catalog_system/pub/products/variations/'

    # busca informações do produto
    response = requests.get(baseURL + productId)
    data = response.json()

    # nome do produto
    name = data['name']
    # preço do produto
    price = data['skus'][0]["bestPriceFormated"]
    # url da imagem do produto
    url = data['skus'][0]['image']

    fileName = 'product:' + datetime.now().strftime("%m-%d-%Y-%H-%M-%S%f") + '.png'
    # busca e salva imagem do produto no arquivo"fileName"
    urllib.request.urlretrieve(url, fileName)

    return {"productId": productId,
            "url": url,
            "imageFileName": fileName,
            "price": price,
            'name': name}
#######################################################
