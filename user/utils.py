from django.shortcuts import render, redirect


class MyProfileEditMixin:
    queryset = None
    form = None
    template_name = None

    def get(self, request):
        qs = self.queryset
        return render(request, self.template_name, {'form': qs})

    def post(self, request):
        return self.form(request)