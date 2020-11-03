from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator


class PieChartAndAddMixin:
    form = None
    post_form = None
    qs = None
    labels = None
    data = None
    template_name = None

    def get(self, request):
        labels = self.labels
        data = self.data
        list_of_purchases = self.qs()
        qs = list_of_purchases[:10]
        try:
            return render(request, self.template_name, {'form': self.form, 'purchases': qs,
                                                        'labels': labels, 'data': data})

        except AttributeError:
            return HttpResponseRedirect('accounts/login/')

    def post(self, request):
        """ПОСТ запрос для записи покупки в БД"""
        return self.post_form(request)


class PurchaseListAndAddMixin:
    """Миксин для отображения списка покупок, формы для их записи и фильтра по дате"""

    queryset = None
    types = None
    template_name = None
    average = None

    def get(self, request):
        """Получаем Форму и Покупки"""
        try:
            return render(request, self.template_name, {'statistics': self.queryset,
                                                        'types': self.types, 'average': self.average})

        except AttributeError:
            return HttpResponseRedirect('accounts/login/')




