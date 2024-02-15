from django.urls import path
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new

from django.conf import settings

from django.views.static import serve

from . import views
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('',views.home),
    path('login',views.custom_login),#เรียกใช้ def ชื่อ custom_login
    path('add_product',views.add_product),
    path('add_type',views.add_type),
    path('manage_product',views.manage_product),
    path('manage_type',views.manage_type),
    path('delete/<int:pk>',views.delete_product),
    path('delete_type/<int:pk>/', views.delete_type, name='delete_type'),
    path('delete_report/<int:pk>/', views.delete_report, name='delete_report'),
    path('edit/<int:pk>',views.edit_product),#หน้าแก้ไขข้อมูลยา
    path('editt/<int:pk>',views.edit_type),#หน้าแก้ไขข้อมูลประเภทยา
    path('increase_qty/<int:pk>',views.increase_product),#หน้าเพิ่มจำนวนยา
    path('decrease_qty/<int:pk>',views.decrease_product),#หน้าลดจำนวนยา
    path('logout/',views.logout_view),
    path('buy_product/', views.buy_product_view, name='buy_product'),
    path('buy_productu/', views.buy_product,),
    path('register/', views.register_view, name='register'),
    path('report', views.report_a,),
    
]