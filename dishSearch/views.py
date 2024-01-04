from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
import json



def showrestaurant(request):
    query = request.GET.get('query')
    restaurants = Restaurant.objects.all()
    object_list = []
    

    if not query:

        # changing the dishes field into dictionary for better manipulation
        for each in list(restaurants):
            each.items = json.loads(each.items)
            if each.aggregate_rating:
                each.aggregate_rating = int(20 * each.aggregate_rating)
            object_list.append({'info':each})
    else:
        query = query.lower()
        # for searching dishes
        for each in restaurants:
            each.items = json.loads(each.items)
            if each.aggregate_rating:
                each.aggregate_rating = int(20 * each.aggregate_rating)
            dish_dict = each.items
            dishes = list(dish_dict.keys())
            for i in range(len(dishes)) :
                # searching for query in every dish, if found appending it to final object list
                if query in dishes[i].lower():
                    dish_info = {'dish':dishes[i], 'info':each}
                    object_list.append(dish_info)

        # for searchin restaurant
        Name_list=restaurants.filter(name__icontains=query)
        for each in Name_list:
            each.items = json.loads(each.items)
            if each.aggregate_rating:
                each.aggregate_rating = int(20 * each.aggregate_rating)
            object_list.append({'info':each})


    object_list = list(object_list)

    # pagination of object_list into bunch of 30s
    college_paginator = Paginator(object_list, 30)
    page_num = request.GET.get('page')
    page = college_paginator.get_page(page_num)
    surl = request.get_full_path()

# Append the search query to the URL as a query parameter
    if query:
        surl += '&'
    else :
        surl = '/showrestaurant?'
    context = {'page': page,'query': query,'surl': surl}
    return render (request,'showrestaurant.html',context)


