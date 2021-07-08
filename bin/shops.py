#!/usr/bin/env python3

import sys
import config

from classes.itad import Itad

itad = Itad(config.itadApiKey)

shops = itad.getShops()

print('Магазины:')

if (shops):
    for shop in shops:
        print(shop['id'])
else:
    print('Ничего не найдено.')