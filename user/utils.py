from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


class MyProfileEditMixin:
    queryset = None
    form = None
    template_name = None

    def get(self, request):
        qs = self.queryset
        try:
            return render(request, self.template_name, {'form': qs})
        except AttributeError:
            return HttpResponseRedirect('/accounts/login/')

    def post(self, request):
        return self.form(request)