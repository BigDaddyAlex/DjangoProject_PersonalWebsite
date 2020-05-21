from .views import homePageView,aboutPageView
from django.urls import path

urlpatterns = [path('',homePageView.as_view(),name='home'),
    path('about/',aboutPageView.as_view(),name='about')
    ]

