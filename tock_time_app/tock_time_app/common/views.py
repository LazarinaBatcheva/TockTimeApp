from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    View for rendering the home page.
    Inherits from TemplateView to handle rendering a static template.
    """

    template_name = 'common/home.html'
