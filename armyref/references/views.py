from django.views.generic import TemplateView

from armies.models import Phase
from references.models import Reference


class HomeView(TemplateView):
    template_name = 'references/home.html'
    game = 'Age of Sigmar'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context.update(title='Welcome to army references!',
                       references=Reference.objects.filter(phase__game__name=self.game))
        return context
