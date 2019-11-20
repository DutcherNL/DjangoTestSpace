from django.views.generic import TemplateView

from .models import Content

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class ContentView(TemplateView):
    template_name = "content.html"
    
    def get_context_data(self, **kwargs):
        context = super(ContentView, self).get_context_data(**kwargs)
        try:
            content = Content.objects.get(id=self.kwargs.get('id', None))
            context['content'] = content.content
        except Content.DoesNotExist:
            context['content'] = "Does not exist"

        return context
