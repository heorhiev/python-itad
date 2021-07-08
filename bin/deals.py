#!/usr/bin/env python3

import sys
import config

from classes.itad import Itad

if len (sys.argv) == 1:
    print('Введите магазины (через запятую):')
    shops = input()
else :
    shops = sys.argv[1]


if shops:
    itad = Itad(config.itadApiKey)

    deals = itad.getDeals(shops, 500) # 500 - количество 

    print('Игры:')

    if (deals):
        for deal in deals:
            print(deal['title'])
            print('  старая цена: ' + str(deal['price_old']))
            print('  новая цена: ' + str(deal['price_new']))
            print('  магазин: ' + deal['shop']['name'])
    else:
        print('Ничего не найдено.')