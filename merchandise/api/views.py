from rest_framework import views, response, status, permissions, exceptions

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
                    'message': f' سفارش شما برای محصول{product}  با موفقیت حذف شد',
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

