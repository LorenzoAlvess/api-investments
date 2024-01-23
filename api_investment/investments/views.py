from django.shortcuts import render

# investments/views.py

from rest_framework import generics
from .models import Investment, Account
from .serializers import InvestmentSerializer, AccountSerializer
from .permissions import IsOwner

class InvestmentListView(generics.ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class AccountListView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DepositView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsOwner]

class WithdrawView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsOwner]


