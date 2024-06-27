from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from Auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
@login_required
def get_user_details(request):
    
    return render(request, 'userprofile/test.html',{'user':request.user,'title':'GreenCart | '+ request.user.first_name})

@login_required
def edit_user_details(request):
    if request.method == 'POST':
        user = request.user
        user = User.objects.get(pk=user.id)
        
        # Try to get the existing user profile, create one if it doesn't exist
        try:
            user_profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile(user=user)
        
        user.first_name = request.POST['first_name']
        
        dob = request.POST.get('dob', '1990-01-01')  # Default date if empty
        if not dob:  # Additional check if dob is still empty
            dob = '1990-01-01'
        user_profile.date_of_birth = dob
        
        user.save()
        user_profile.save()
        
        message = 'Profile Updated Successfully'
        messages.success(request, message)
        return redirect('userprofile:get_user_details')
