from django.urls import path
from . import views

urlpatterns = [
    path('doktoraty/', views.DoktoratListView.as_view(), name='doktorat_list'),
    path('doktoraty/nowy/', views.DoktoratCreateView.as_view(), name='doktorat_create'),
    path('doktoraty/<int:pk>/', views.DoktoratDetailView.as_view(), name='doktorat_detail'),
    path('doktoraty/<int:pk>/edytuj/', views.DoktoratUpdateView.as_view(), name='doktorat_update'),
    path('doktoraty/<int:pk>/usun/', views.DoktoratDeleteView.as_view(), name='doktorat_delete'),
]
