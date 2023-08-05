
from django.urls import path,include
from .  import views

urlpatterns = [
   
    path('',views.index, name='index'),
    path('books',views.books, name='books'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
]
