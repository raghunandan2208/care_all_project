from django.urls import path
from dashboard.views import dashboard, younger_request, elder_approval, reject_approval, history, payment

urlpatterns = [

    path('', dashboard, name='dashboard'),
    path('request/<int:user_id>', younger_request, name='younger_request'),
    path('approve/<int:user_id>', elder_approval, name='elder_approval'),
    path('reject/<int:user_id>', reject_approval, name='reject_approval'),
    path('history/<int:id>', history, name='history'),
    path('payment/<int:id>', payment, name='payment'),

]
