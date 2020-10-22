from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from services.main_logic import user_is_anonymous


class PurchaseListAndAddMixin:
    """Миксин для отображения списка покупок, формы для их записи и фильтра по дате"""
    form = None
    post_form = None
    queryset = None
    types = None
    template_name = None
    average = None

    def get(self, request):
        """Получаем Форму и Покупки"""
        try:
            return render(request, self.template_name, {'form': self.form, 'statistics': self.queryset,
                                                        'types': self.types, 'average': self.average})

        except AttributeError:
            return HttpResponseRedirect('accounts/login/')

    def post(self, request):
        """ПОСТ запрос для записи покупки в БД"""
        return self.post_form(request)


