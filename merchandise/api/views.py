from rest_framework import views, response, status, permissions, exceptions, generics

from merchandise.models import MiniOrder


class DeleteMiniOrderAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, pk, *args, **kwargs):
        try:
            order = MiniOrder.objects.get(pk=pk)
            producer = order.product.producer
            if request.user == producer.user:
                name = order.name
                product = order.product.title
                order.delete()
                data = {
                    'message': f' سفارش شما برای محصول {product}  با موفقیت حذف شد',
                }
                return response.Response(data,
                                         status=status.HTTP_200_OK)
            else:
                data = {
                    'message': "شما دسترسی به این صفحه ندارید"
                }
                return response.Response(data,
                                         status=status.HTTP_401_UNAUTHORIZED)
        except exceptions.NotAuthenticated:
            return response.Response({'message': 'شما به این صفحه دسترسی ندارید'},
                                     status=status.HTTP_401_UNAUTHORIZED)

class ConfirmMiniOrder(views.APIView):

    def get(self, request, pk, *args, **kwargs):
        try:
            order = MiniOrder.objects.get(pk=pk)
            phone_number = order.phone_number
            producer = order.product.producer.user
            if request.user == producer:
                order.is_confirmed = True
                order.save()
                data = {
                    'message' : 'سفارش شما با موفقیت تایید شد',
                    'status' : True,
                    'phone_number' : phone_number,
                }
                return response.Response(data,
                            status=status.HTTP_200_OK)
            else:
                data = {
                    'message' : "شما به این سفارش دسترسی ندارید",
                    'status' : False,
                }
                return response.Response(
                    data, status=status.HTTP_401_UNAUTHORIZED
                )
        
        except exceptions.NotAuthenticated:
            return response.Response(
                {
                    'message' : 'شما به این صفحه دسترسی ندارید'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )