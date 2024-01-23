# investments/urls.py

from django.urls import path
from .views import InvestmentListView, InvestmentDetailView, AccountListView, AccountDetailView, DepositView, WithdrawView

urlpatterns = [
    path('investments/', InvestmentListView.as_view(), name='investment-list'),
    path('investments/<int:pk>/', InvestmentDetailView.as_view(), name='investment-detail'),
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('accounts/<int:pk>/deposit/', DepositView.as_view(), name='account-deposit'),
    path('accounts/<int:pk>/withdraw/', WithdrawView.as_view(), name='account-withdraw'),
]
