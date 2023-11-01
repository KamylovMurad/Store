from django.urls import path
from .views import CreateVisitView, StoreListView

app_name = 'visits'

urlpatterns = [
    path('stores/<str:phone_number>/', StoreListView.as_view(), name='store-list'),
    path('visits/<str:phone_number>/', CreateVisitView.as_view(), name='create-visit')
]
