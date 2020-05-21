from .views import homePageView,aboutPageView,contactPageView
from django.urls import path

urlpatterns = [path('',homePageView.as_view(),name='home'),
    path('about/',aboutPageView.as_view(),name='about'),
    path('contact/',contactPageView.as_view(),name='contact')
    ]

