from .views import homePageView,aboutPageView,get_msg,thanksPageView
from django.urls import path

urlpatterns = [path('',homePageView.as_view(),name='home'),
    path('about/',aboutPageView.as_view(),name='about'),
    path('contact/',get_msg,name='contact'),
    path('contact/thanks/',thanksPageView.as_view(),name='thanks')
    ]

