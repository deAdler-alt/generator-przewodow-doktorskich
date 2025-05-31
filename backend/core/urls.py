from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('doktoraty/', views.DoktoratListView.as_view(), name='doktorat_list'),
    path('doktoraty/nowy/', views.DoktoratCreateView.as_view(), name='doktorat_create'),
    path('doktoraty/<int:pk>/', views.DoktoratDetailView.as_view(), name='doktorat_detail'),
    path('doktoraty/<int:pk>/edytuj/', views.DoktoratUpdateView.as_view(), name='doktorat_update'),
    path('doktoraty/<int:pk>/usun/', views.DoktoratDeleteView.as_view(), name='doktorat_delete'),
# Logowanie i wylogowanie
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dokumenty/nowy/', views.DokumentCreateView.as_view(), name='dokument_create'),
    path('historia/nowa/', views.HistoriaCreateView.as_view(), name='historia_create'),
]
