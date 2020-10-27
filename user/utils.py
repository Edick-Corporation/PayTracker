from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


class MyProfileMixin:
    queryset = None
    context_object_name = None
    template_name = None

    def get(self, request):
        if request.user.is_anonymous:
            return HttpResponseRedirect('/accounts/login/')

        else:
            return render(request, self.template_name, {self.context_object_name: self.queryset})


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