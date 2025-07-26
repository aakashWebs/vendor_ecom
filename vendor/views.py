from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, ProductSerializer, CategorySerializer
from store.models import Product, Category
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render
from vendor.tasks import fetch_data_from_api
import requests

class VendorRegisterView(APIView):
    permission_classes = []

    def get(self, request):
        return Response({"detail": "Send a POST request with username, email, and password to register."})
    
    # def post(self, request):
        #  response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        #  fetch_data_from_api.delay('https://jsonplaceholder.typicode.com/posts')
        #  return Response({'status':1}, status=200)


    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data.get('email'),
                password=request.data.get('password')
            )
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorLoginView(ObtainAuthToken):
    def get(self, request, *args, **kwargs):
        return Response({"detail": "Send a POST request with username and password to login."})

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({'token': token.key, 'user_id': user.id, 'username': user.username})

class VendorDashboardView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        products = Product.objects.filter(vendor=user)
        categories = Category.objects.filter(vendor=user)
        products_serializer = ProductSerializer(products, many=True)
        categories_serializer = CategorySerializer(categories, many=True)
        return Response({
            'products': products_serializer.data,
            'categories': categories_serializer.data
        })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vendor_logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)

def api_register_view(request):
    return render(request, 'vendor/api_register.html')

def api_login_view(request):
    return render(request, 'vendor/api_login.html')
