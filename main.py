from getProductInformations import getProductInformations
from createCatalog import createCatalog
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--productsId', nargs='+', type=int)
args = parser.parse_args()

if not args.productsId or len(args.productsId) != 3:
    print("erro de uso: utilize a opção -p ou --productsId para informar os ids dos produtos que deseja gerar um catalogo ")
    exit(1)
    pass
products = []
for prodId in args.productsId:
    products.append(getProductInformations(str(prodId)))


createCatalog(products)
