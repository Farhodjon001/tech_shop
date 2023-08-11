from django.urls  import path
from .views import PaymentListCreateApiView,PcListCreateApiView,PaymentDetailUpdateDeleteApiView,PcDetailUpdateDeleteApiView,GetSoldPcApiView

urlpatterns=[
    path("pc/",PcListCreateApiView.as_view()),
    path("pc/<int:pk>/",PcDetailUpdateDeleteApiView.as_view()),
    path("payment/",PaymentListCreateApiView.as_view()),
    path("payment/<int:pk>",PaymentDetailUpdateDeleteApiView.as_view()),
    path("sold/<str:day>/",GetSoldPcApiView.as_view())

]