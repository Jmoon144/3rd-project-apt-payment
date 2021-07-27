#from django.urls import path, include
#
#from .views import PublicPaymentList, AdminPaymentViewSet
#
#admin_payment_list = AdminPaymentViewSet.as_view({
#    'get'  : 'list',
#    'post' : 'create'
#})
#
#admin_payment_detail = AdminPaymentViewSet.as_view({
#    'get'    : 'retrieve',
#    'put'    : 'update',
#    'delete' : 'destroy'
#})
#
#urlpatterns = [
#    path('admin/', admin_payment_list),
#    path('admin/<int:pk>', admin_payment_detail),
#    path('public/', PublicPaymentList.as_view()),
#    path('api-auth/', include('rest_framework.urls'))
#]
