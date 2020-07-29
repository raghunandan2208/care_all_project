from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib.auth.decorators import login_required
from accounts.models import Elder,Younger, YoungerRequest, ElderApproval, Transactions, Completed, Profile
from django.contrib import messages
from accounts.views import elder_profile
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from star_ratings.models import Rating



# Create your views here.

@login_required
def dashboard(request):
    current_user = request.user
    user_type = None

    if current_user.is_younger:
        user_type = 'Younger'
    else:
        user_type = 'Elder'

    help_seekers = Elder.objects.filter(need_help=True)
    request_by_younger = YoungerRequest.objects.filter(request_to=current_user.id)
    elder_profile = Profile.objects.get(user = current_user.id)

    if current_user.is_elder:
        elder = Elder.objects.get(user_id=current_user.id)
    else:
        elder = None

    try:
        trans = Transactions.objects.get(care_seeker=current_user.id)
        profile = Profile.objects.get(user=trans.care_giver.user)

    except ObjectDoesNotExist:
        print("No Record Found")
        trans = None
        profile = None

    try:
        dash_rating = Rating.objects.get(object_id=current_user.id)

    except ObjectDoesNotExist:
        print("No Record Found")
        dash_rating = None

    # profile = Profile.objects.get(user=user_id)

    context = {
            'current_user' : current_user,
            'user_type' : user_type,
            'help_seekers': help_seekers,
            'request_by_younger' : request_by_younger,
            'trans': trans,
            'elder_profile': elder_profile,
            'dash_rating': dash_rating,
            'elder': elder,
            'profile': profile,

                }
    return render(request, 'dashboard/dashboard.html', context)


def younger_request(request, user_id, *args, **kwargs):
    younger_id = request.user
    younger = Younger.objects.get(user_id=younger_id)
    elder = Elder.objects.get(user_id=user_id)

    count = YoungerRequest.objects.filter(request_by=younger).count()

    if YoungerRequest.objects.filter(request_by = younger, request_to=elder).exists():
        messages.error(request, 'You have been requested , please be patient for response')
        print("Hello old man")
    else:
        if count < 4:
            m = YoungerRequest(request_by=younger, request_to=elder)
            m.save()
            messages.success(request, 'Your request is sent succcessfully...')
        else:
            messages.error(request, 'You already have 4 requests')


    return redirect('/dashboard')


def elder_approval(request, user_id, *args, **kwargs):
    elder = request.user
    elder_id = elder.id
    elder_instance = Elder.objects.get(user_id = elder_id)
    balance = Elder.objects.get(user_id=elder_id).funds
    younger = Younger.objects.get(user_id=user_id)
    count =ElderApproval.objects.filter(approved_by=elder_id).count()
    print(younger)
    younger_count = ElderApproval.objects.filter(approved_to=younger).count()



    date = datetime.now()+timedelta(days=7)
    duration = (date-datetime.now()).days
    amount_to_pay = (duration)*550

    if ElderApproval.objects.filter(approved_by=elder_id).exists():
        messages.error(request, 'You already have one caretaker')
    else:
        if count==1:
            messages.error(request, 'you already have a care taker as of now')
        else:
            if balance >= 5000 and younger_count < 4:
                m = ElderApproval(approved_by=elder_instance, approved_to=younger)
                t = Transactions(care_seeker=elder_instance, care_giver=younger,end_date=date,duration=duration, amount_to_pay=amount_to_pay)
                e = Elder.objects.get(user_id=elder_id)
                e.need_help = False
                m.save()
                t.save()
                e.save()
                messages.success(request, 'Care Taker assigned to you succcessfully...')

            else:
                if balance < 5000:
                    messages.error(request, 'Please maintain minimum balance of Rs. 5000 in your wallet')
                else:
                    messages.error(request, 'Younger has 4 care seekers')

    # YoungerRequest.objects.filter(request_by=younger, request_to=elder_instance).delete()
    return redirect('/dashboard')



def reject_approval(request, user_id, *args, **kwargs):
    elder_id = request.user
    elder = Elder.objects.get(user_id=elder_id)
    younger = Younger.objects.get(user_id=user_id)
    YoungerRequest.objects.filter(request_by=younger, request_to=elder).delete()
    return redirect('/dashboard')


def payment(request,id,*arg, **kwargs):
    now = timezone.now()
    user = Transactions.objects.get(care_seeker=id)
    t_id  = user.id
    elder_appr_id = ElderApproval.objects.get(approved_by=id).id
    duration = (user.end_date-user.date_approved).days
    amount = (duration)*550
    younger_instance=user.care_giver
    elder = Elder.objects.get(user_id=id)
    elder_balance = Elder.objects.get(user_id=elder).funds
    pay = elder_balance-amount
    younger_balance = Younger.objects.get(user_id=younger_instance).earnings
    younger_tot_bal = younger_balance + amount
    elder_balance_up = Elder.objects.filter(user_id=elder).update(funds=pay)
    younger_earnings = Younger.objects.filter(user_id=younger_instance).update(earnings=younger_tot_bal)
    comp = Completed.objects.create(care_to=elder,
                                    care_by=younger_instance,
                                    date_started=user.date_approved,
                                    scheduled_end_date=user.end_date,
                                    date_ended=timezone.now(),
                                    duration=duration,
                                    amount_paid=amount)

    delete_Transactions = Transactions.objects.filter(id=t_id).delete()

    delete_elderApproval = ElderApproval.objects.filter(id=elder_appr_id).delete()
    bill = Completed.objects.filter(care_to=id).order_by('-id')[0]

    context = {

        'bill':bill

        }
    return render(request,'dashboard/payment.html',context)


def history(request,id,*args, **kwargs):
    history = Transactions.objects.filter(care_seeker=id)
    comp = Completed.objects.filter(care_to=id).order_by('-id')
    y_history = Transactions.objects.filter(care_giver=id)
    y_comp = Completed.objects.filter(care_by=id).order_by('-id')
    context = {
        'history':history,
        'comp':comp,
        'y_history': y_history,
        'y_comp': y_comp
        }

    return render(request,'dashboard/history.html',context)
