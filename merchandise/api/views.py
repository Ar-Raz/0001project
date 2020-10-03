from rest_framework import views, response, status, permissions

from merchandise.models import MiniOrder

from website.mixins import GroupRequiredMixin

class DeleteMiniOrderAPIView(views.APIView, GroupRequiredMixin):
    permission_classes = [permissions.IsAuthenticated,]

    group_required = 'Producer'

    def get(self, request, pk, *args, **kwargs):
        order = MiniOrder.objects.get(pk=pk)
        producer = order.product.producer
        if request.user == producer.user:
            name = order.name
            product = order.product.title
            order.delete()
            data = {
                'message': f' سفارش شما برای محصول{product}  با موفقیت حذف شد',
            }
            return response.Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'message': f""
            }
            return response.Response()

