from django.urls import path, include
from accounts.views import UserCreateView,YoungerSignUpView,ElderSignUpView,changeStatus, profile_page, profile_details, younger_profile, elder_profile, ContactFormView, GuestContactFormView, add_money_to_wallet, changeStatus
from django.contrib.auth.views import (LoginView,
                                        LogoutView,
                                        PasswordResetView,
                                        PasswordResetDoneView,
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView,
                                        PasswordChangeView,
                                        PasswordChangeDoneView,
                                        )


urlpatterns = [

    path('login/', LoginView.as_view(template_name = "accounts/login.html"), name='login'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('signup_form/younger/', YoungerSignUpView.as_view(), name='younger_signup'),
    path('signup_form/elder/', ElderSignUpView.as_view(), name='elder_signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('changestatus/',changeStatus,name='change_status'),
    path('addfund/',add_money_to_wallet,name='addfund'),
    # path('', include('django.contrib.auth.urls')),
    path('password-reset/', PasswordResetView.as_view(template_name="accounts/password_reset_form.html", email_template_name="accounts/password_reset_email.html"), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="accounts/password_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name='password_reset_complete'),
    path('password-change/', PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    # path('profile/<str:user>', ProfileView.as_view(), name='profile'),

    path('profile/<int:id>', profile_details, name='profile'),
    path('profile-update/', profile_page, name='profile-update'),
    path('younger-profile/<int:user_id>/', younger_profile, name='younger_profile'),
    path('elder-profile/<int:user_id>/', elder_profile, name='elder_profile'),
    path('contacts', ContactFormView.as_view(), name='contacts'),
    path('guest-contactus', GuestContactFormView.as_view(), name='guest_contacts'),


]
