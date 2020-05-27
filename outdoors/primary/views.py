from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from portfoliosite import settings


class ProjecttwoView(TemplateView):
    template_name = 'projecttwo/projecttwo.html'
