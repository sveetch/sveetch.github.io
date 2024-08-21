from gettext import gettext as _

from optimus.pages.views import PageTemplateView


class GenericPageView(PageTemplateView):
    """
    Basic page view.
    """
    title = _("Generic basic page")
    template_name = "generic.html"
    destination = "{language_code}/index.html"
