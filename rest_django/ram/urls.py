from django.urls import path
from ram import views

urlpatterns=[
    path('BookList/',views.BookList),
    path('Bookpost/',views.Bookpost),
    path('Bookupdate/<int:pk>/',views.Bookupdate),
    path('Bookdelete/<int:pk>/',views.Bookdelete),
]