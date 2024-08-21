from .data import DataView
from .generic import GenericPageView


# Enabled pages to build
PAGES = [
    # Sample view with default language and forces a destination
    GenericPageView(destination="index.html"),

    # Sample view for french language
    GenericPageView(lang="fr"),

    # Sample for pure data view
    DataView(),
]
