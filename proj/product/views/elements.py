# from django.shortcuts import HttpResponse
# from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
# # new
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
#
# from product.models import Likes, Category, Product, Cmments, Favourite
# from product.serializers import (
# )
# from tasks.filters import TaskFilter
#
#
# class ProductAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#
#     def get(self, request):
#         product_list = request.user.product_set.all()
#         filtered = ProductFilter(request.GET, product_list)
#
#
#
