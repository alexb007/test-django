from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.views import ProductList, ReviewApiView

router = DefaultRouter()
router.register(r'product_list', ProductList, basename='product-list')

urlpatterns = router.urls

urlpatterns += [
    path('reviews/<int:pk>/', ReviewApiView.as_view()),
]
