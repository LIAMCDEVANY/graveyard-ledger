from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('entries/', views.entry_index, name='entry-index'),
    path('entries/create/', views.entry_create, name='entry-create'),
    path('entries/<int:entry_id>/update/', views.entry_update, name='entry-update'),
    path('entries/<int:entry_id>/delete/', views.entry_delete, name='entry-delete'),
    path('entries/<int:entry_id>/', views.entry_detail, name='entry-detail'),
]