from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView

from . import forms
from django.shortcuts import HttpResponseRedirect
from . import models
from django.views import View


# Create your views here.

class IndexView(CreateView):
    model = models.FeedbackModel
    form_class = forms.FeedbackForm
    template_name = 'feedback/first_form.html'
    success_url = '/feedback_sent'

    #def form_valid(self, form):
    #    form.save()
    #    return super(IndexView, self).form_valid(form)


class Index(View):
    def get(self, request):
        form = forms.FeedbackForm()
        return render(request, 'feedback/first_form.html', context={'form': form})

    def post(self, request):
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/feedback_sent')


class FeedbackSentView(TemplateView):
    template_name = 'feedback/successfully_sent_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_update = models.FeedbackModel.objects.last()
        context['name'] = recent_update.name
        context['surname'] = recent_update.surname
        return context


class EdgarView(View):
    def get(self, request):
        form = forms.EdgarForm()
        return render(request, 'feedback/edgar.html', context={'form': form})

    def post(self, request):
        form = forms.EdgarForm(request.POST)
        if form.is_valid():

            form.save()
            if form.cleaned_data['name'] == 'edgar':
                return HttpResponseRedirect('/yesgar')
            return render(request, 'feedback/edgar.html', context={'form': form, 'traitor': True})


class YesgarView(TemplateView):
    template_name = 'feedback/yesgar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_update = models.EdgarModel.objects.last()
        context['surname'] = recent_update.surname
        return context


class InstanceEditingView(View):
    def get(self, request, feedback_id):
        feedback_instance = models.FeedbackModel.objects.get(
            id=feedback_id)  # по айдишнику отбирается строка в таблице в бд
        form = forms.FeedbackForm(instance=feedback_instance)
        return render(request, 'feedback/first_form.html', context={'form': form})

    def post(self, request, feedback_id):
        feedback_instance = models.FeedbackModel.objects.get(
            id=feedback_id)  # по айдишнику отбирается строка в таблице в бд
        form = forms.FeedbackForm(request.POST,
                                  instance=feedback_instance)  # по отобранной строке заполняется форма на странице
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{feedback_id}')

class FieldUpdateView(UpdateView):
    form = forms.FeedbackForm
    model = models.FeedbackModel
    template_name = 'feedback/first_form.html'
    success_url = '/'
    fields = '__all__'

# class FeedbackListView(TemplateView):
#    template_name = 'feedback/list_feedback.html'
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        feedbacks = models.FeedbackModel.objects.all()
#        context['feedbacks'] = feedbacks
#        return context

class FeedbackListView(ListView):
    template_name = 'feedback/list_feedback.html'
    model = models.FeedbackModel
    context_object_name = 'feedbacks'



class FeedbackDetailedView(DetailView):
    template_name = 'feedback/detailed_feedback.html'
    model = models.FeedbackModel
