import os
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime


def createCatalog(productsInformations, background_color='red'):
    # background
    background = Image.open("catalogo3.png")

    # image draw
    draw = ImageDraw.Draw(background)

    # image draw font
    font = ImageFont.truetype('arial.ttf', 36)

    # product image size

    # image positions
    imagesPositions = [(307, 435), (89, 1237),
                       (580, 1237)]
    imagesLength = [(487, 477), (407, 407), (407, 402)]
    namesPositions = [(309, 950), (87, 1660), (579, 1660)]
    priceCirclePisitions = [(660, 820, 890, 1035),
                            (380,  1555, 550, 1730), (880,  1555, 1055, 1730)]
    pricesPositions = [(705, 900), (400, 1610), (900, 1610)]

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

        # circulo do preço
        draw.ellipse(priceCirclePisitions[cont], fill='blue')

        nameWidth, nameHeight = font.getsize(product['imageFileName'])

        nameToWrite = product['name']

        for i in range(2):
            section = nameToWrite[:23]
            sectionPos = (namesPositions[cont][0],
                          namesPositions[cont][1] + 65*(i))
            end = section.rfind(" ")
            draw.text(
                sectionPos, nameToWrite[:end], font=font, fill='white')
            nameToWrite = nameToWrite[end+1:]

        # preço
        draw.text(
            pricesPositions[cont], product['price'], font=font, fill='white')
        cont += 1

    fileName = 'catalog:' + datetime.now().strftime("%m-%d-%Y-%H-%M-%S%f") + '.png'
    background.save(fileName)
    print("seu catalogo foi criado e salvo no diretório atual com o seguinte nome:\n"+fileName)
###########################################################################
