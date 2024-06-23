from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def get_user_details(request):
    
    return render(request, 'userprofile/profile.html',{'user':request.user})

@login_required
def add_user_details(request):
    if request.method == 'POST':
        user = request.user
        user_profile = user.userprofile
        user_profile.date_of_birth = request.POST.get('dob')
        user_profile.bio = request.POST.get('bio')
        user_profile.address_line_1 = request.POST.get('address_line_1')
        user_profile.address_line_2 = request.POST.get('address_line_2')
        user_profile.city = request.POST.get('city')
        user_profile.state = request.POST.get('state')
        user_profile.country = request.POST.get('country')
        user_profile.zip_code = request.POST.get('zip_code')
        user_profile.phone_number = request.POST.get('phone_number')
        user_profile.profile_pic = request.FILES.get('profile_pic')
        user_profile.save()
        return render(request, 'userprofile/user_profile.html',{'title':request.user.first_name,'user':request.user})
    return render(request, 'userprofile/add_user_details.html',{'title':request.user.first_name,'user':request.user})