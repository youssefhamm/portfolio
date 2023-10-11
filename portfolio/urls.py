from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inner-page/', views.inner_page, name='inner-page'),
    path('portfolios-details/', views.portfolio_details, name='portfolio-details'),
]
