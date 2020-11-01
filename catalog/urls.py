from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
  path('', views.index),
  path('samochody/', views.cars),
  path('samochody/najstarsze', views.oldest_cars),
  path('samochody/najmlodsze', views.newest_cars),
  path('samochody/jezdzace', views.riding_cars),
  path('samochody/stojace', views.staying_cars),
  path('samochody/zkierowca', views.driver_cars),
  path('samochod/<int:car_id>', views.car_details),
  path('kontakt/', views.contact),
  path("zamawiane/", views.cart),
  path("zamawiane/add", views.add_to_cart),
  path("zamawiane/remove", views.remove_from_cart),
  path("order/", views.order),
  path("order/<int:order_id>", views.order_details),
  path("clean_card/", views.clean_card),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
        serve, {'document_root': settings.MEDIA_ROOT, }),]