from django.shortcuts import render,redirect
from django.views.generic import CreateView, DetailView, UpdateView, FormView
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm, YoungerSignUpForm, ElderSignUpForm, ProfileUpdateForm, UserUpdateForm, ContactForm
from django.contrib.auth.decorators import login_required
from accounts.models import User, Elder, Younger, Profile
from django.contrib.auth import login
from star_ratings.models import Rating
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def index(request):
    return render(request, 'index.html')

def thankyou(request):
    return render(request, 'accounts/thankyou.html')

def guest_thankyou(request):
    return render(request, 'accounts/guest_thankyou.html')

class UserCreateView(CreateView):
    template_name = "accounts/signup.html"
    form_class = SignUpForm
    success_url = "/accounts/login/"


class YoungerSignUpView(CreateView):
    model = User
    form_class = YoungerSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'younger'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/accounts/login/')


class ElderSignUpView(CreateView):
    model = User
    form_class = ElderSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'elder'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/accounts/login/')


def profile_details(request, *args, **kwargs):
    id = request.user.profile.id
    o_id = request.user.id
    profile = Profile.objects.get(id = id)
    print(o_id)
    try:
        rating = Rating.objects.get(object_id=o_id)
        print(rating)
    except ObjectDoesNotExist:
        rating = None
        print("Not found")

    context = {
    'profile' : profile,
    'rating': rating
    }
    return render(request, 'profile/profile.html', context)


def younger_profile(request, user_id, *args, **kwargs):
    profile = Profile.objects.get(user=user_id)
    print(user_id)
    try:
        rating = Rating.objects.get(object_id=user_id)
        print(rating)
    except ObjectDoesNotExist:
        rating = None
        print("Not found")
    context = {
        'profile':profile,
        'rating':rating
    }
    return render(request, 'profile/profile.html', context)


def elder_profile(request, user_id, *args, **kwargs):
    profile = Profile.objects.get(user=user_id)
    try:
        rating = Rating.objects.get(object_id=user_id)
    except ObjectDoesNotExist:
        rating = None
        print("not found")
    context = {
        'profile':profile,
        'rating':rating
    }
    return render(request, 'profile/profile.html', context)


def profile_page(request, *args, **kwargs):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        print(request.user)

    context = {
        'user_form':user_form,
        "profile_form" : profile_form
    }
    return render(request, 'profile/profile-update.html', context)


def changeStatus(request,*args, **kwargs):
    id = request.user
    elder = Elder.objects.get(user=id)
    print(elder)
    print(id)
    # need_help = False
    if elder.need_help:
        messages.success(request, 'Your are In-Active now')
        elder.need_help = False
        elder.save()

    else:
        messages.success(request, 'Your are Active now')
        elder.need_help = True
        elder.save()

    return redirect('/dashboard')


def add_money_to_wallet(request,*args, **kwargs):
    user = request.user.id
    print(user)
    try:
        younger_earnings = Younger.objects.get(user_id=user).earnings
    except:
        younger_earnings = None
    try:
        qs = Elder.objects.get(user_id=user)
    except:
        qs = None

    print(qs)

    if 'addfund' in request.GET:
        addfund = request.GET['addfund']
        if addfund:
            qs.add_fund(int(addfund))
            qs.save()
            messages.success(request, 'Amount added to your wallet successfully...')


    context = {

        'younger_earnings':younger_earnings
        }
    return render(request,'accounts/addfund.html',context)


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = "/thankyou"
    template_name = "accounts/contactus.html"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class GuestContactFormView(FormView):
    form_class = ContactForm
    success_url = "/guest_thankyou"
    template_name = "accounts/guest_contactus.html"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
