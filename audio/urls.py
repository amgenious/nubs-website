from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about'),
    path('wings', views.wings, name='wings'),
    path('gallery', views.gallery, name='gallery'),
    path('academic', views.academic, name='academic'),
    path('sermon', views.sermon, name='sermon'),
    path('sunday_sermon', views.sunday_sermon, name='sunday_sermon'),
    path('tuesday_studies', views.tuesday_studies, name='tuesday_studies'),
    path('thursday_prayers', views.thursday_prayers, name='thursday_prayers'),
    
]
