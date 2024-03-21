from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RequisitionForm, ApprovalForm
from django.contrib.auth.decorators import login_required
from .models import Requisition
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request,
                username = username,
                password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Req:submit_requisition')
                else:
                    return redirect('No Such account')
            else:
                return redirect('Req:login')
    else:
        form = LoginForm()

    return render(request, 'Req/login.html', {'form':form}) 

@login_required
def approve_requisition(request, request_id):
    approval_request = get_object_or_404(Requisition, pk=request_id)
    if approval_request.user == request.user:
        return redirect("Req:submit_requisition")
    decision_form = ApprovalForm(instance=approval_request)
    
    if request.method == 'POST' and 'approve' in request.POST:
        decision_form = ApprovalForm(request.POST, instance=approval_request)
        if decision_form.is_valid():
            approval_decision = decision_form.cleaned_data['approved']
            if approval_decision:
                 send_approval_email(approval_request)
            else:
                send_rejection_email(approval_request)
            return redirect('Req:submit_requisition')
    context = {'approval_request':approval_request,'decision_form':decision_form}
    return render(request, 'Req/approve_requisition.html', context)

@login_required
def submit_requisition(request):
    unapproved_requests = Requisition.objects.filter(approved=False)
    if request.method == 'POST':
        approval_form = RequisitionForm(request.POST)
        if approval_form.is_valid():
            requisition = approval_form.save(commit=False)
            requisition.user = request.user
            requisition.save()
            return redirect('Req:submit_requisition')
    else:
        approval_form = RequisitionForm()

    context = {'approval_form': approval_form, 'unapproved_requests':unapproved_requests}
    return render(request, 'Req/submit_requisition.html', context)

@login_required
def approval(request):
    if request.method == 'POST':
        form = ApprovalForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Req:approve_requisition')
    else:
        form = ApprovalForm()
    return render(request, 'Req/approval.html', {'form': form})

@login_required
def send_approval_email(approval_request):
    subject = 'Requisition Approved - Request ID {}'.format(approval_request.id)
    to_email = [approval_request.user.email]
    from_email = 'Nifoluwa@mail.com'
    html_message = render_to_string('Req/approval_email.html', {'approval_request': approval_request})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

def send_rejection_email(approval_request):
    subject = f'Requisition Rejected - Request ID {approval_request.id}'
    to_email = [approval_request.user.email]
    from_email = 'Nifoluwa@mail.com'
    html_message = render_to_string('Req/rejection_email.html', {'approval_request': approval_request})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
    

@login_required
def custom_logout(request):
    logout(request)
    return redirect('Req:login')