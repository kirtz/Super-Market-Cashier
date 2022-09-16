from dis import dis
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
            product = input ('Enter Product: ') #Getting Product data
            quantity = int(input('Enter quantity: ')) #Qauntity of products
            buyingData.update({product: quantity}) #Update the dictionary 
        elif details == 'Q': #To Quit the loop (stop buying)
            enterDetails = False
        else:
            print('Please select a correct option') #let user know to input correct information
        return buyingData

        
# Getting the price of products function

def getPrice (product, quantity): #Predefined Dictionary of products 
    
    #Product name = Key and Price of product in £'s
    priceData = {  
        'Biscuit': 5,
        'Chicken': 7,
        'Egg': 2,
        'Fish': 6,
        'Coke': 5,
        'Bread': 5,
        'Apple': 4,
        'Onion': 4,
        'Water': 2,
    }

#Subtotal = Product name: £Price X Qauntity 

    subtotal = priceData[product] * quantity
    print(product + ':£' + str(priceData[product]) + 'x' + str(quantity)) + '=' + str(subtotal)
    return subtotal

#Discount function

def getDiscount(billAmount, membership):
    discount = 0
    #Nested If statement to figure out customers membership and apply membership discounts
    if billAmount >= 40: 
        if membership == 'Gold':
            billAmount = billAmount * 0.80
            discount = 20
        elif membership == 'Silver':
            billAmount = billAmount * 0.90
            discount = 10 
        elif membership == 'Bronze':
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) +  '% off for' + membership + ' ' + 'membership on total amount: £' + str(billAmount))
    #If purchase is < £40, no discount is aplied 
    else:
        print('No discount on amount less than £25')
        return billAmount

#Final bill Function

def makeBill(buyingData, membership):   #Bill function with 2 parameters - Dictionary of products purchased by consumer
    # + membership status of consumer

    billAmount = 0 #declare and initialize the variable which holds the subtotal amount of consumer.
    for key, value in buyingData.items(): #Calculate the subtotal,with the Key and value, pass through getPrice to find the product and price 
        billAmount += getPrice(key, value) #for loop since getPrice will get info of one product at a time
    billAmount = getDiscount(billAmount, membership) #subtotal of all the products, time to deduct discount by checking membership status
    print('The discounted amount is £' + str(billAmount))