from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from search.models import Products
from django.db.models import Max, Q
from django.contrib import messages
from .forms import StoreForm,BrandForm,TitleForm
from django.core.urlresolvers import reverse
import re
from django.contrib import messages


# Create your views here.
def home(request):
    products = Products.objects.all()
    #template_name = search/products_list.html
	#context_object = "products_list"
    return render(request, 'search/products_list.html',{ 'Products_list' : products })
	

    
def max_price(request):
    #max_prices = Products.objects.all().aggregate(Max('price'))
    #price = Products.objects.values('price')
	#max_price = max(price)
    #for i,v in max_prices.items():
    #    max_price = v
    #max_product = Products.objects.filter(price=max_price)
    max_product = Products.objects.order_by('-price').first()
    message = "Maximum Price is"
    return render(request, 'search/max.html', {'Maximum_Product' : max_product, 'Message' : message})
	

	
def store_display(request):
   
    store = Products.objects.values('store').distinct()

    return render(request, 'search/store_display.html', { 'stores' : store})
	
	
	
def store_details(request,store_id):
   
    #Advert.objects.values_list('city', flat=True).distinct()
    products = Products.objects.filter(store=store_id)
          
    return render(request, 'search/store_details.html', { 'products' : products })

	
	
def store_unique(request):

    store_uniq = Products.objects.values('store').filter( in_stock=False).distinct().order_by('store')
    return render(request, 'search/store_unique.html', {'stores' : store_uniq})

	
	
def brand_display(request):
    
    if request.method == 'POST':
    
        brandForm = BrandForm(request.POST)
        if brandForm.is_valid():
            price = brandForm.cleaned_data['price_range']

            return HttpResponseRedirect(reverse('brand_price', kwargs={'price_range': price}))
        else:
            print("Form in Not Valid")
    else:
        brandForm = BrandForm()
        return render(request, 'search/brand_display.html', { 'form' : brandForm})
	
	
	
def brand_price(request,price_range):
      
    first_char = price_range[0]
    if first_char == '<':
        price = price_range.split("<")
        
        #brand_list = Products.objects.filter(price__lte=price[1]).values('brand').distinct()
        brand_list = Products.objects.filter(price__lte=price[1]).values('brand')
        

    elif first_char == '>':
        price = price_range.split(">")
        
        #brand_list = Products.objects.filter(price__gte=price[1]).values('brand').distinct()
        brand_list = Products.objects.filter(price__gte=price[1]).values('brand')
        
    else:
        ranges = price_range.split("-")   
        #for r in ranges:
        #    print("Value is", r)
        if len(ranges) == 2:
            #brand_list = Products.objects.filter(price__range=[ranges[0],ranges[1]]).values('brand').distinct()
            brand_list = Products.objects.filter(price__range=[ranges[0],ranges[1]]).values('brand')
         
   
    return render(request, 'search/brand_price.html', { 'brands' : brand_list , 'price_range' : price_range})
	
	
def title_search(request):
    
    if request.method == 'POST':

        form = TitleForm(request.POST)
        if form.is_valid():
            stock = form.cleaned_data['in_stock']
            brand = form.cleaned_data['brand']
            store = form.cleaned_data['store']
            print("brand,store,stock", stock,brand,store)
            if store is not None:
                return HttpResponseRedirect(reverse('product_titles', kwargs={'stock' : stock, 'brand' : brand, 'store' : store}))
            else:
                return HttpResponseRedirect(reverse('product_titles', kwargs={'stock' : stock, 'brand' : brand}))

    
    form = TitleForm()
    
    return render(request, 'search/title_get.html', {'form' : form})

		
def product_titles(request,stock,brand,store=None):
    
    if store is None:
        titles = Products.objects.filter(in_stock=stock,brand=brand).values('title')

        if titles:
            return render(request, 'search/product_titles.html', {'titles' : titles })
        else:
            return  render(request, 'search/product_error.html')
    else:
        titles = Products.objects.filter(Q(in_stock=stock),Q(brand=brand)|Q(store=store)).values('title')
        
        if titles:
            return render(request, 'search/product_titles.html', {'titles' : titles })
        else:
             return  render(request, 'search/product_error.html')   