from .views import homePageView,aboutPageView,ContactView,thanksPageView
from django.urls import path

urlpatterns = [path('',homePageView.as_view(),name='home'),
    path('about/',aboutPageView.as_view(),name='about'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('contact/thanks/',thanksPageView.as_view(),name='thanks')
    ]

