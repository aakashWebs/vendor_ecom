from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Category, Product
from django.shortcuts import get_object_or_404

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'store/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendor = self.request.user
        context['categories'] = Category.objects.filter(vendor=vendor)
        context['products'] = Product.objects.filter(vendor=vendor)
        return context

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'store/category_list.html'

    def get_queryset(self):
        return Category.objects.filter(vendor=self.request.user)

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'store/category_form.html'
    success_url = reverse_lazy('store:category_list')

    def form_valid(self, form):
        form.instance.vendor = self.request.user
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    template_name = 'store/category_form.html'
    success_url = reverse_lazy('store:category_list')

    def get_queryset(self):
        return Category.objects.filter(vendor=self.request.user)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'store/category_confirm_delete.html'
    success_url = reverse_lazy('store:category_list')

    def get_queryset(self):
        return Category.objects.filter(vendor=self.request.user)

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'store/product_list.html'

    def get_queryset(self):
        return Product.objects.filter(vendor=self.request.user)

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'category', 'tags']
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('store:product_list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # Limit category choices to vendor's categories
        form.fields['category'].queryset = Category.objects.filter(vendor=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.vendor = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'category', 'tags']
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('store:product_list')

    def get_queryset(self):
        return Product.objects.filter(vendor=self.request.user)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['category'].queryset = Category.objects.filter(vendor=self.request.user)
        return form

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = reverse_lazy('store:product_list')

    def get_queryset(self):
        return Product.objects.filter(vendor=self.request.user)
