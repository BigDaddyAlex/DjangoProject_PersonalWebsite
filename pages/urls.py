from .views import homePageView,aboutPageView,get_msg,thanksPageView,projectsPageView,get_topic
from django.urls import path

urlpatterns = [path('',homePageView.as_view(),name='home'),
    path('addtopic',get_topic,name='addtopic'),
    path('about/',aboutPageView.as_view(),name='about'),
    path('contact/',get_msg,name='contact'),
    path('contact/thanks/',thanksPageView.as_view(),name='thanks'),
    path('projects/',projectsPageView.as_view(),name='projects')
    ]

