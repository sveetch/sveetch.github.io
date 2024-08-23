from gettext import gettext as _

from optimus import __version__
from optimus.pages.views import PageTemplateView


class GenericPageView(PageTemplateView):
    """
    Basic page view.
    """
    title = _("Generic basic page")
    template_name = "generic.html"
    destination = "{language_code}/index.html"

    def get_destination(self):
        """
        Return build file destination depending language.

        The file will be built to a sub directory named after current language if it
        is not the default one.

        Returns:
            string: Either the value of ``template_name`` or ``LANGUAGE/template_name``.
        """
        lang = self.get_lang()

        if lang.code != self.settings.LANGUAGE_CODE:
            return "{}/{}".format(lang.code, self.destination)

        return self.destination

    def get_context(self):
        """
        Add Optimus version.
        """
        super().get_context()

        self.context.update({
            "optimus_version": __version__,
        })
        return self.context