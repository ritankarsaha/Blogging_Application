from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('reports/', views.reports, name='reports'),
    path('policy/', views.policy, name='policy'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/upvote/', views.upvote_post, name='upvote_post'),
    path('<slug:slug>/clap/', views.clap_post, name='clap_post'),
    
]
