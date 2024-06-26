"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

handler404 = 'listings.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('bands/', views.band_list, name='bands'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/update/', views.band_update, name='band-update'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),


    
    path('about-us/', views.about),
    
    path('listings/', views.listings, name='listings'),
    path('listings/<int:listing_id>/', views.listing_detail, name='listing-detail'),
    path('listings/add/', views.listing_create, name='listing-create'),
    path('listings/<int:id>/update/', views.listing_update, name='listing-update'),
    path('listings/<int:id>/delete/', views.listing_delete, name='listing-delete'),
    
    path('contact-us/', views.contact, name='contact'),
    path('confirmation/', views.confirmation, name='confirmation'),
  ]
