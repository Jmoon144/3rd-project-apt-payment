#from django.contrib.auth.models import User
#
#from .serializer import AdminPaymentSerializer, PublicPaymentSerializer
#from .models     import Payment
#
#from rest_framework             import generics, viewsets
#from rest_framework.permissions import IsAdminUser, IsAuthenticated
#
#class AdminPaymentViewSet(viewsets.ModelViewSet):
##        permission_classes = [IsAdminUser]
#        queryset           = Payment.objects.all()
#        serializer_class   = AdminPaymentSerializer
#
#class PublicPaymentList(generics.ListAPIView):
#        permission_classes = [IsAuthenticated]
#        serializer_class   = PublicPaymentSerializer
#
#        def get_queryset(self):
#                user = self.request.user
#                return user.payment_set.all()
