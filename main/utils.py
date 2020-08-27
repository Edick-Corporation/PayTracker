from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


class PurchaseListAndAddMixin:
    """Миксин для отображения списка покупок и формы для их записи"""
    form = None
    model = None
    template_name = None

    def get(self, request):
        """Получаем список покупок и форму"""
        if request.user.is_anonymous:
            print('anonymous')
            return redirect('account_login')
        else:
            form = self.form
            purchase_list = self.model.objects.filter(user=request.user.profile.pk)
            return render(request, self.template_name, {'form': form, 'purchases': purchase_list})

    def post(self, request):
        """ПОСТ запрос для записи покупки в БД"""
        if request.user.is_anonymous:
            print('anonymous')
            return redirect('purchase_list')
        else:
            if request.method == 'POST':
                form = self.form(request.POST)
                if form.is_valid():
                    purchase = form.save(commit=False)
                    purchase.user = request.user.profile
                    purchase.save()
                    return redirect('purchase_list')
