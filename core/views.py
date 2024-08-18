from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Product, Review
from core.serializers import ProductSerializer, ReviewSerializer


class ProductList(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category', 'color', 'price',)
    search_fields = ('title', 'description',)
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset.filter(active=True)


class ReviewApiView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None, *args, **kwargs):
        product = self.get_object(pk)
        reviews = Review.objects.filter(product=product)
        rates = reviews.values_list('rate', flat=True)
        result = []
        for rate in rates:
            result.append({'rate': rate, 'items': ReviewSerializer(reviews.filter(product=product), many=True).data})
        return Response(result)
