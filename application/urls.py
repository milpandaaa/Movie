from django.urls import path, include
from django.urls import reverse
from .views import *


urlpatterns = [
    path('', base, name='base_url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/<int:user_id>/', account, name='account_url'),
    path('selling/<int:user_id>/<int:cassette_id>/', selling, name='selling_url'),
    path('sort/<str:theme>/', sort, name='sort_url'),
    path('singup', signup, name='signup_url'),
    path('cassetteAdd', cassetteAdd, name='cassetteAdd_url'),
    path('sellerAdd', sellerAdd, name='sellerAdd_url'),
    path('sellers', sellers, name='sellers_url'),
    path('admissionAdd/<int:seller_id>/', admissionAdd, name='admissionAdd_url'),
    path('sellerDelete/<int:seller_id>/', sellerDelete, name='sellerDelete_url'),
    path('cassetteDelete/<int:cassette_id>/', cassetteDelete, name='cassetteDelete_url'),
    path('forDelete', forDelete, name='forDelete_url'),
]