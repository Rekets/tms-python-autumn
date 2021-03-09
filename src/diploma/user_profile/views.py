import profile

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import View

from django.views.generic import DeleteView, \
    UpdateView, DetailView, FormView

from home.models import Articles
from user_profile.forms import ActivityForm
from user_profile.models import Activity, Profile


class UserDetailView(DetailView):
    """
    Детали профиля
    """
    model = User
    template_name = 'user/profile.html'
    slug_field = 'username'
    slug_url_kwarg = "username"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        print(context)
        context['activity'] = Activity.objects.filter(user=context['user'])
        print(context['activity'])
        return context


def edit_profile(request, username):
    print(request.POST)
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.country = request.POST.get('country')
        profile.weight = request.POST.get('weight')
        profile.height = request.POST.get('height')
        profile.birth_date = request.POST.get('birth_date')
        profile.avatar = request.POST.get('avatar')
        user.save()
        profile.save()
    return render(request, "user/edit_profile.html", {"user": user})


class UserDeleteView(DeleteView):
    """
    Удаление профиля
    """
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'user/delete_profile.html'
    success_url = '/'


class RegisterFormView(FormView):
    """
    Класс регестрирования новго профиля
    """
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "user/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.

        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    """
    Класс аутентификации нового пользователя
    """
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = 'user/login.html'

    # В случае успеха перенаправим на главную.
    success_url = '/start/'

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect(
            reverse('home'))


def see_activity(request):
    """
    Функция просмотра ленты активностей
    """
    activity = Activity.objects.order_by('-date')

    return render(request, 'user/activity.html', {'activity': activity})


def create(request):
    """
    Функция создание новой активности и добавления на сайт
    :return: новая запсить на сайте во вкладке 'Activity'
    """

    if request.method == 'POST':
        form = ActivityForm(request.POST)

        # высчитываем потраченные колории #

        calories = int(request.POST.get('rout_length')) * int(
            request.POST.get('weight'))
        Activity.calories = calories

        # высчитываем суммарное расстояние #

        all_length_list = (
            Activity.objects.filter(
                user__username__contains=request.POST.get('user')).values_list(
                'rout_length', flat=True))
        # print(all_length_list)
        all_length_int = []
        for i in all_length_list:
            i = int(i)
            all_length_int.append(i)
        all_length = sum(all_length_int) + int(
            request.POST.get('rout_length'))
        # print(all_length)
        Activity.all_length = all_length

        # высчитываем суммарное время #

        all_duration_list = (
            Activity.objects.filter(
                user__username__contains=request.POST.get('user')).values_list(
                'duration', flat=True))
        # print(all_duration_list)
        all_duration_int = []
        for q in all_duration_list:
            q = int(q)
            all_duration_int.append(q)
        all_duration = sum(all_duration_int) + int(
            request.POST.get('duration'))
        # print(all_duration)
        Activity.all_duration = all_duration

        # высчитываем среднюю скорость #

        av_speed = round(int(request.POST.get('rout_length')) / (int(
            request.POST.get('duration')) / 60), 1)
        Activity.av_speed = av_speed

        if form.is_valid():
            request.calories = Activity.calories
            request.all_length = Activity.all_length
            request.all_duration = Activity.all_duration
            request.av_speed = Activity.av_speed
            form.save(request.user, request.calories, request.all_length,
                      request.all_duration, av_speed)

            return redirect('activity')

    return render(request, 'user/create.html')
