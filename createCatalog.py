from PIL import Image, ImageFont, ImageDraw
import os
from math import ceil
from getProductInformations import getProductInformations


def createCatalog(productsInformations, background_color='red'):
    # background
    background = Image.open("catalogo3.png")

    # image draw
    draw = ImageDraw.Draw(background)

    # product image size

    # image positions
    imagesPositions = [(307, 435), (89, 1237),
                       (580, 1237)]
    imagesLength = [(487, 477), (407, 407), (407, 402)]
    namesPositions = [(309, 950), (87, 1660), (579, 1660)]
    priceCirclePisitions = [(660, 820, 890, 1035),
                            (380,  1555, 550, 1730), (880,  1555, 1055, 1730)]
    pricesPositions = []

    cont = 0

    for product in productsInformations:
        # adiciona imagem ao catalogo
        productImage = Image.open(product['imageFileName'])

        productImage = productImage.resize(imagesLength[cont])
        productImage = productImage.copy()
        background.paste(productImage, (imagesPositions[cont]))

        productImage.close()
        os.remove(product['imageFileName'])

        # adiciona nome do produto e preço ao catalogo
        font = ImageFont.truetype('arial.ttf', 36)
        nameWidth, nameHeight = font.getsize(product['imageFileName'])

        nameToWrite = product['name']

        for i in range(2):
            section = nameToWrite[:25]
            sectionPos = (namesPositions[cont][0],
                          namesPositions[cont][1] + 65*(i))
            end = section.rfind(" ")
            draw.text(
                sectionPos, nameToWrite[:end], font=font, fill='white')
            nameToWrite = nameToWrite[end+1:]

        # circulo do preço
        draw.ellipse(priceCirclePisitions[cont], fill='blue', outline='blue')

        # preço

        cont += 1

    background.save('final.png')
###########################################################################


products = []

products.append(getProductInformations("3"))
products.append(getProductInformations("5"))
products.append(getProductInformations("12"))

createCatalog(products)
