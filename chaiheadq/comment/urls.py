from django.urls import path

from chaiheadq.comment import views
urlpatterns = [
    
    path('', views.comments_list,name='comments_list'),
    path('create/',views.comment_create,name='comment_create'),
    path('<int:comment_id>/edit/',views.comment_edit,name='comment_edit'),
    path('<int:comment_id>/delete/',views.comment_delete,name'comment_delete'),
    path('registration/',views.registration,name='registration'),
    
]
    
