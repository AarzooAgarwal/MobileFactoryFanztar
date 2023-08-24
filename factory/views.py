
# Create your views here.
from factory.constants import CONSTANTS
from factory.controllers.mobile_factory import CreateOrderController
from factory.serializers.mobile_factory import CreateOrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateOrder(APIView):
    def post(self, request):
        validation = CreateOrderSerializer(data=request.data)
        validation.is_valid(raise_exception=True)
        
        order_resp = CreateOrderController().create_order(request.data)
        
        code, msg = CONSTANTS.GENERIC.SUCCESS
        response = {
            "status": code,
            "message": msg,
            "data": order_resp
        }
        
        return Response(response, status=status.HTTP_200_OK)