import os
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def personal_info(request):
    try:
        if request.method == "POST":
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            user_name = request.POST['user_name']
            email = request.POST['email_address']
            password = request.POST['password']
            gender = request.POST['gender']
            image = request.FILES.get('image')
            t_area = request.POST['t_area']
            if image:
                if user_name:
                    value = p_info.objects.create(f_name=f_name, l_name=l_name, user_name=user_name, email=email,
                                                  password=password, gender=gender, image=image, t_area=t_area)
                    value.save()
                    return redirect('index')
                else:
                    messages.error(request, 'please fill the user name')
                    return redirect('personal_info')
            else:
                value = p_info.objects.create(f_name=f_name, l_name=l_name, user_name=user_name, email=email,
                                              password=password, gender=gender, t_area=t_area)
                value.save()
                return redirect('index')

    except:
        messages.error(request, 'please fill all elements')
        return redirect('personal_info')

    return render(request, 'personal_info.html')


@login_required(login_url='login')
def profile(request):
    try:

        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            gender = request.POST['gender']
            image = request.FILES.get('image')

            if image:
                if first_name:
                    value = prof.objects.create(first_name=first_name, last_name=last_name, email=email,
                                                password=password,
                                                gender=gender, image=image)
                    value.save()
                    return redirect('index')
                else:
                    messages.error(request, 'plz fillup the first name')
                    return redirect('profile')
            else:
                value = prof.objects.create(first_name=first_name, last_name=last_name, email=email, password=password,
                                            gender=gender)
                value.save()
                return redirect('index')
    except:
        messages.error(request, 'plz fillup all field')
        return redirect('profile')

    return render(request, 'profile.html')


@login_required(login_url='login')
def all_iteams(request):
    search = request.GET.get('search')

    if search:
        all_pinfo = p_info.objects.filter(Q(l_name__icontains=search) | Q(email__icontains=search))
        all_prof = prof.objects.filter(Q(last_name__icontains=search) | Q(email__icontains=search))
    else:
        all_pinfo = p_info.objects.all()
        all_prof = prof.objects.all()

    context = {
        'all': all_pinfo,
        'all_prof': all_prof,
    }
    return render(request, 'all_iteams.html', context)


@login_required(login_url='login')
def persoprofdel(request, id):
    persoprfdel = p_info.objects.get(id=id)
    if persoprfdel.image != 'default/default.jpg':
        os.remove(persoprfdel.image.path)
    persoprfdel.delete()
    return redirect('all_iteams')


@login_required(login_url='login')
def profdel(request, id):
    profdel = prof.objects.get(id=id)
    if profdel.image != 'default/default.jpg':
        os.remove(profdel.image.path)
    profdel.delete()
    return redirect('all_iteams')


@login_required(login_url='login')
def update_p_profile(request, id):
    var_prof = p_info.objects.get(id=id)

    if request.method == "POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        user_name = request.POST['user_name']
        email = request.POST['email_address']
        password = request.POST['password']
        gender = request.POST['gender']
        image = request.FILES.get('image')
        t_area = request.POST['t_area']

        if image:
            if var_prof.image != 'default/default.jpg':
                os.remove(var_prof.image.path)
            var_prof.f_name = f_name
            var_prof.l_name = l_name
            var_prof.user_name = user_name
            var_prof.email_address = email
            var_prof.password = password
            var_prof.gender = gender
            var_prof.image = image
            var_prof.t_area = t_area

            var_prof.save()
            messages.success(request, 'update done')
            return redirect('all_iteams')
        else:
            var_prof.f_name = f_name
            var_prof.l_name = l_name
            var_prof.user_name = user_name
            var_prof.email_address = email
            var_prof.password = password
            var_prof.gender = gender
            var_prof.t_area = t_area

            var_prof.save()
            messages.success(request, 'update done')
            return redirect('all_iteams')

    return render(request, 'update_perinfo.html', locals())


@login_required(login_url='login')
def update_profile(request, id):
    var_prof = prof.objects.get(id=id)

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        image = request.FILES.get('image')
        if image:
            if var_prof.image != 'default/default.jpg':
                os.remove(var_prof.image.path)
            var_prof.first_name = first_name
            var_prof.last_name = last_name
            var_prof.email = email
            var_prof.password = password
            var_prof.gender = gender
            var_prof.image = image
            var_prof.save()
            messages.success(request, 'update done')
            return redirect('all_iteams')
        else:
            var_prof.first_name = first_name
            var_prof.last_name = last_name
            var_prof.email = email
            var_prof.password = password
            var_prof.gender = gender
            var_prof.save()
            messages.success(request, 'update done')
            return redirect('all_iteams')
    return render(request, 'update_prof.html', locals())
