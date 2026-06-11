from django.urls import path

from product.views import product_create, product_delete, product_list, product_update


urlpatterns = [
    path('list',product_list),
    path('create',product_create),
    path('update/<int:id>',product_update),
    path('delete/<int:id>',product_delete),
]