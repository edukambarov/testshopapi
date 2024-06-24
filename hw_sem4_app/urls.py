from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shop_main, name='main'),
    path('shop_add_good/', views.add_good, name='add_good'),
    path('shop_sales_report/<int:client_id>/<int:days>/',
         views.sort_orders_of_the_client_by_date_and_distinct_products,
         name='report')
]
