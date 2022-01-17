from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView
admin.autodiscover()


from . import views

urlpatterns = [
    path('', views.index, name='index'),
  
    # # ex: /polls/5/
    # path('<int:pose_id>/name/', views.name, name='name'),
    # # ex: /polls/5/results/
    # path('<int:pose_id>/category/', views.category, name='category'),
    # # ex: /polls/5/vote/
    # path('<int:pose_id>/email/', views.email, name='email'),
]