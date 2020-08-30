from django.shortcuts import render, redirect

from services.main_logic import get_form_to_record_purchase, add_purchase, user_is_anonymous


class PurchaseListAndAddMixin:
    """Миксин для отображения списка покупок, формы для их записи и фильтра по дате"""
    form = None
    queryset = None
    template_name = None

    def get(self, request):
        """Получаем Форму и Покупки"""
        try:
            return render(request, self.template_name, {'form': self.form, 'statistics': self.queryset})
        except AttributeError:
            return redirect('account_login')

    def post(self, request):
        """ПОСТ запрос для записи покупки в БД"""
        return add_purchase(self, request)