from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'traders', 
        view = views.TradersListView.as_view(), 
        name = "traders.index"
    ),
    path(
        route ='traders/<int:pk>', 
        view = views.TradersDetailView.as_view(),
        name = 'traders.detail'
    ),
    path(
        route ='traders/new',
        view = views.TradersCreateView.as_view(),
        name = 'traders.new'
    ),path(
        route ='traders/<int:pk>/update', 
        view = views.TradersUpdateView.as_view(),
        name = 'traders.update'
    ),
    path(
        route ='traders/<int:pk>/delete', 
        view = views.TradersDeleteView.as_view(),
        name = 'traders.delete'
    ),
]
