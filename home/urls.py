from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ListMatiz.as_view(), name='home'),
    path('search/', views.SearchList.as_view(), name='search'),
    path('search_new/', views.NewSearchList.as_view(), name='search_new'),
    path('new_matiz/', views.NewListMatiz.as_view(), name='new_matiz'),
    path('about/', views.about, name='about'),
    path('callform/', views.callform, name='callform'),
    path('success_callform', views.success_callform, name='success_callform'),
    path('detail/<int:pk>', views.MatizDetailView.as_view(), name='detail'),
    path('basket/<int:id>', views.basket, name='basket'),
    path('basket_add/<int:matiz_id>', views.basket_add, name='basket_add'),
    path('basket_delete/<int:id>', views.basket_delete, name='basket_delete'),
    path('pay/<int:id>', views.pay, name='pay'),
    path('pay_success/', views.pay_success, name='pay_success')

]