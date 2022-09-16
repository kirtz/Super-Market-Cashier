import unicodedata
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from itertools import product
from statistics import quantiles


# Entering the products purchase + quantity 

def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input ('Press A to add prodct and Q to quit')
        if details == 'A':
            product = input ('Enter Product: ')
            quantity = int(input('Enter quantity: '))
            buyingData.update({product: quantity})
        elif details == 'Q':
            enterDetails = False
        else:
            print('Please select a correct option')
        return buyingData