from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^max/$',views.max_price, name='max_price'),
    url(r'^store_display/$',views.store_display, name='store_display'),
    url(r'^store_details/(?P<store_id>\d+)$',views.store_details, name='store_details'),
    url(r'^store_unique/$',views.store_unique, name='store_unique'),
    url(r'^brand_display/$',views.brand_display, name='brand_display'),
    url(r'^brand_price/(?P<price_range>.*)$',views.brand_price, name='brand_price'),
    url(r'^title_search/$',views.title_search, name='title_search'),
    url(r'^product_titles/(?P<stock>\w+)/(?P<brand>\d+)$',views.product_titles, name='product_titles'),
    url(r'^product_titles/(?P<stock>\w+)/(?P<brand>\d+)/(?P<store>\d+)$',views.product_titles, name='product_titles'),
]
from django.conf.urls import url

