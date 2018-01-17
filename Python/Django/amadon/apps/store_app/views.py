# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


def index(request):
    context = {'products':{
        '1':{
            'name': 'hairbrush',
            'price': 2.99},
        '2':{
            'name': 'diamond hairbrush',
            'price': 2000.99},
        '3':{
            'name': 'used barbie hairbrush',
            'price': 1.99},
        '4':{
            'name': 'old beef/ lb',
            'price': 4.59},
        '5':{
            'name': 'beef hairbrush',
            'price': 20.99},
    }}

    request.session['products'] = context['products']
    return render(request, 'store_app/index.html', context)

def billing(request):
    if request.method == 'POST':
        product_id = request.POST['id']
        name = request.session['products'][product_id]['name']
        quantity = request.POST['quantity']
        price = request.session['products'][product_id]['price']
        cost = price * float(quantity)

        order = {
            'id':product_id,
            'name':name,
            'quantity':quantity,
            'price':price,
            'cost':cost,
        }
        request.session['order'] = order
        print "here's where I bill your credit card for " + str(cost) + " clams plus a 10 clams processesing fee."

	return redirect('/checkout')

def checkout(request):

	return render(request, 'store_app/checkout.html')