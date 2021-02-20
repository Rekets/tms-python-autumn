from django.shortcuts import render, redirect
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
from user_profile.models import Activity


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
        context['articles'] = Articles.objects.filter(author=context['user'])
        return context


class UserUpdateView(UpdateView):
    """
    Измененение профиля
    """
    model = User
    template_name = 'user/edit_profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user'
    fields = ['first_name', 'last_name']
    success_url = '/start/'


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
    activity = Activity.objects.order_by('-date')
    return render(request, 'user/activity.html', {'activity': activity})


def create(request):
    """
    Функция создание новой активности и добавления на сайт
    :return: новая запсить на сайте во вкладке 'Activity'
    """

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start-work')

    form = ActivityForm()
    data = {
        'form': form,
    }

    return render(request, 'user/create.html', data)
