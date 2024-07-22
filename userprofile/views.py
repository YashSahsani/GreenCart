from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from Auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserForm, UserProfileForm
# Create your views here.


@login_required
def get_user_details(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            # Redirect or add a success message
    else:
        user_form = UserForm(instance=user)
        user_profile_form = UserProfileForm(instance=user_profile)
    return render(request, 'userprofile/profile.html', {
        'user_form': user_form,
        'user_profile': user_profile,
        'user_profile_form': user_profile_form,
        'title': 'GreenCart | ' + request.user.first_name,
        'user_profile_pic': user_profile.profile_pic.url,
    })

@login_required
def edit_user_details(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if  user_form.has_changed() or user_profile_form.has_changed() and user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('userprofile:get_user_details')
        elif not user_form.has_changed() and not user_profile_form.has_changed():
            messages.warning(request, 'No changes were made')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        user_form = UserForm(instance=request.user)
        user_profile = UserProfile.objects.get_or_create(user=request.user)
        user_profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'userprofile/profile.html', {
        'title': 'GreenCart | ' + request.user.first_name,
        'user_form': user_form,
        'user_profile_form': user_profile_form,
        'user_profile_pic': user_profile.profile_pic.url,
    })