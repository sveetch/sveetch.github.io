import json
from pathlib import Path

from .generic import GenericPageView


class HomepageView(GenericPageView):
    """
    The homepage view.
    """

    title = "Homepage"
    destination = "index.html"
    template_name = "homepage.html"
    datas = ["registry.json"]

    def get_registry(self):
        """
        Open and parse tools registry.

        Returns:
            dict: A dictionnary with distincts items for tool kinds:

                * ``cookiecutters`` for cookiecutter templates;
                * ``applications`` for applications;
        """
        source = Path(self.settings.DATAS_DIR) / "registry.json"
        return json.loads(source.read_text())

    def get_context(self):
        """
        Append registry items to template context

        Returns:
            dict: The context dict.
        """
        super().get_context()

        self.context.update(**self.get_registry())

        return self.context
