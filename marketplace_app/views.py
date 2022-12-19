from django.shortcuts import render
from django.core.paginator import Paginator

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination

from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from django.db.models import Q

class MyPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'results': data,
        })


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    pagination_class = MyPagination

    def list(self, request):
        queryset = Product.objects.all().order_by('SKU')
        data = request.GET.copy()
        print("Sdata ", data)
        # DATA
        category = data.get('category')
        keyword = data.get('keyword')
        order = data.get('order')
        print(category, keyword, order)
        # FILTERS
        if category: queryset = queryset.filter(Q(category__name__icontains=category))
        if keyword: queryset = queryset.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword))
        print("ORDER ", order)
        # ORDERING
        if order and order in ['higherPrice', 'lowerPrice', 'nameAsc', 'nameDesc']: 
            
            if order == 'lowerPrice':
                queryset = queryset.order_by('-price')
            if order == 'higherPrice':
                queryset = queryset.order_by('price')
            if order == 'nameAsc':
                queryset = queryset.order_by('name')
            if order == 'nameDesc':
                queryset = queryset.order_by('-name')

        # PAGINATE N' SERIALIZE
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Category.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)