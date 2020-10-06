from rest_framework import views, status
from rest_framework.response import Response


from pages.models import NewsTellerEmails


class NewsTellerCreateAPIView(views.APIView):

    def post(self, request, format=None, *args, **kwargs):
        email = request.POST.get('email')
        if email:
            qs = NewsTellerEmails.objects.filter(email=email)
            if qs.exists():
                return Response({'message' : 'شما از پیش عضو خبرنامه هستید'}, status=status.HTTP_200_OK)
            else:
                obj = NewsTellerEmails.objects.create(email=email)
                obj.save()
                return Response({'message' : 'شما با موفقیت عضو خبرنامه دمیر شدید'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message' : 'لطفا فیلد ایمیل را به درستی پر کنید'}, status=status.HTTP_400_BAD_REQUEST)

