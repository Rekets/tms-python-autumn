from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def profile(request, username):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        return render(request, 'user/profile.html', {'user': user})
    else:
        return HttpResponse(
            f'Stop watching from the sidelines, register and start making'
            f' yourself!',
            404)


def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        user.username = request.POST.get('username')
        profile = user.profile
        profile.birth_date = request.POST.get('birth_date')
        profile.country = request.POST.get('country')
        profile.height = request.POST.get('height')
        profile.weight = request.POST.get('weight')
        user.save()
        profile.save()
    return render(request, "user/edit_profile.html", {'user': user})


def delete_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        user.delete()
        return render(request, 'user/successfully_delete_profile')
    return render(request, 'user/delete_profile.html', {"user":user})