from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.timezone import now, timedelta
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, password_validation, update_session_auth_hash
from .models import Requirements,Schedule
from .forms import RequirementForm,ScheduleForm
from django.http import JsonResponse

ALLOWED_USERS = ['admin_hr', 'hr_mysore']  #if we need then we can add userrnames


def index(request):
    
    Requirements.objects.filter(created_at__lt=now().date() - timedelta(days=31)).delete() # Clean up old requirements
    today = now().date()
    yesterday = today - timedelta(days=1)
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)

    date_filter = request.GET.get('date')
    requirements = Requirements.objects.all()

    if date_filter == "today": 
        requirements = requirements.filter(created_at__date=today)
    elif date_filter == "yesterday":
        requirements = requirements.filter(created_at__date=yesterday)
    elif date_filter == "last_week":
        requirements = requirements.filter(created_at__date__gte=last_week)
    elif date_filter == "last_month":
        requirements = requirements.filter(created_at__date__gte=last_month)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = list(requirements.values(
            'id', 'company_id', 'company_name', 'bachelor_degree', 'stream', 'percentage',
            'year_of_passout', 'salary', 'agreement', 'location', 'no_of_vacancies', 'created_at'
        ))
        return JsonResponse({'requirements': data})

    scheduleinfo = Schedule.objects.all()
    return render(request, 'index.html', {
        'requirements': requirements,
        'schedule': scheduleinfo,
        'active_filter': date_filter,
        'title': 'Hiring Dashboard',
    })


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get('username')
        if username in ALLOWED_USERS:
            if form.is_valid():
                form.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
            else:
                messages.error(request, 'Invalid form submission.')
        else:
            messages.error(request, 'You are not eligible to register.')
    else:
        initial_data = {'username': '', 'password1': '', 'password2': ''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html', {'form': form,'title':'Register'})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url or 'index')
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = AuthenticationForm()
        form.fields['username'].initial = ''
        form.fields['password'].initial = ''

    return render(request, 'auth/login.html', {'form': form,'title':'LogIn'})


def reset_password_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('reset_password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return redirect('reset_password')

        try:
            password_validation.validate_password(password1, user)
        except Exception as e:
            messages.error(request, f"Password error: {e}")
            return redirect('reset_password')

        user.set_password(password1)
        user.save()

        update_session_auth_hash(request, user)
        messages.success(request, "Your password has been successfully updated.")
        return redirect('login')

    return render(request, 'auth/reset_password.html',{'title':'Reset Password'})


def logout_view(request):
    logout(request)
    return redirect('index') 


def add_requirement(request):
   form = None
   if request.user.is_authenticated:
      if request.method == 'POST':
         if 'reset' in request.POST:
               return redirect('add_requirement')  
         form = RequirementForm(request.POST)
         if form.is_valid():
               form.save()
               messages.success(request, "Requirement added successfully!")
               form = form
               return redirect('index')
      else:
         form = RequirementForm() 
   else:
      return redirect('login') 

   return render(request, 'add_requirement.html', {'form': form,'title':'Add Requirement'})

def update_requirement(request, id):
    requirement = get_object_or_404(Requirements, id=id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RequirementForm(request.POST, instance=requirement)
            if form.is_valid():
                form.save()
                messages.success(request, "Requirement updated successfully!")
                return render(request, 'update_requirement.html', {
                    'form': form,
                    'requirement': requirement,
                    'title': 'Update Requirement',
                    'updated': True
                })
        else:
            form = RequirementForm(instance=requirement)
        return render(request, 'update_requirement.html', {
            'form': form,
            'requirement': requirement,
            'title': 'Update Requirement'
        })

def delete_requirement(request, id):
    requirement = get_object_or_404(Requirements, id=id)
    if request.user.is_authenticated:
        requirement.delete()
        messages.success(request, "Requirement deleted successfully!")
        return redirect('index')
    else:
        return HttpResponse("Unauthorized", status=401)
    

def add_schedule(request):
   form = None
   if request.user.is_authenticated:
      if request.method == 'POST':
         if 'reset' in request.POST:
               return redirect('schedule')  
         form = ScheduleForm(request.POST)
         if form.is_valid():
               form.save()
               messages.success(request, "Scheduled Student list added successfully!")
               form = form
               return redirect('/#schmain')
      else:
         form = ScheduleForm() 
   else:
      return redirect('login') 

   return render(request, 'add_schedule.html', {'form': form,'title':'Add Scheduled Students'})

def schedule(request):
    scheduleinfo=Schedule.objects.all() 
    sname=None
    addr=None
    print(type(scheduleinfo[0].students_name))
    context={
            'schedule':scheduleinfo,
            'addr':addr,
            'updated':None,
            'sname':sname 
    }
    return render(request,'schedules.html',context)
    

# def update_schedule(request,id):
#     schedule = get_object_or_404(Schedule, id=id)
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = ScheduleForm(request.POST, instance=schedule) 
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Schedule updated successfully!")
#                 return redirect('/#schmain')
#                 return render(request, 'add_schedule.html', {
#                     'form': form,
#                     'schedule': schedule,
#                     'title': 'Update Schedule',
#                     'updated': True
#                 })
#         else:
#             form = ScheduleForm(instance=schedule)
#         return render(request, 'add_schedule.html', {
#             'form': form,
#             'requirement': schedule,
#             'title': 'Update Schedule'
#         })
        
def delete_schedule(request,id):
    data = Schedule.objects.get(id=id)
    data.delete()
    return redirect('/#schmain')

def delete_all_schedule(request):
    Schedule.objects.all().delete()
    return redirect('/#schmain')






    
