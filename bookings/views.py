from django.shortcuts import render, render_to_response
from django.views.generic import View


# Create your views here.

class HomeView(View):

    def get(self, request):
        return render_to_response('index.html', locals())

class GalleryView(View):

    def get(self, request):
        return render_to_response('gallery.html', locals())

class AboutView(View):

    def get(self, request):
        return render_to_response('about.html', locals())

class TestimonyView(View):

    def get(self, request):
        return render_to_response('testimony.html', locals())

class AboutView(View):

    def get(self, request):
        return render_to_response('about.html', locals())