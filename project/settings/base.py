"""
Base settings file for development.
"""
import os
from webassets import Bundle

# Enable debug mode
DEBUG = True

# Common site name and domain to use available in templates
SITE_NAME = "Sveetch Github home"
SITE_DOMAIN = "localhost"

# Repository root path is computed from current settings file
REPOSITORY_DIR = os.path.normpath(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "..",
        "..",
    )
)

# Base site project path
PROJECT_DIR = os.path.normpath(
    os.path.join(
        REPOSITORY_DIR,
        "project",
    )
)

# Directory where the data files will be searched
DATAS_DIR = os.path.join(PROJECT_DIR, "datas")
# Sources directory where the assets will be searched
SOURCES_DIR = os.path.join(PROJECT_DIR, "sources")
# Templates directory
TEMPLATES_DIR = os.path.join(SOURCES_DIR, "templates")
# Directory where all stuff will be builded
PUBLISH_DIR = os.path.join(REPOSITORY_DIR, "dist", "dev")
# Path where will be moved all the static files, usually this is a directory in
# the ``PUBLISH_DIR``
STATIC_DIR = os.path.join(PUBLISH_DIR, "static")
# Path to the i18n messages catalog directory
LOCALES_DIR = os.path.join(PROJECT_DIR, "locale")

# Python path to the views module which enables page views to build
PAGES_MAP = "views"

# Locale name for default language
LANGUAGE_CODE = "en"

# A list of locale name for all available languages to manage with PO files
LANGUAGES = (LANGUAGE_CODE, "fr")

# Babel extraction configuration
I18N_EXTRACT_MAP = (
    ("views/**.py", "python"),
    ("settings/**.py", "python"),
    ("**/templates/**.html", "jinja2"),
)

# The static url to use in templates and with webassets
# This can be a full URL like http://, a relative path or an absolute path
STATIC_URL = "static/"

# Extra or custom bundles
BUNDLES = {
    "layout_css": Bundle("css/layout.css", filters=None, output="css/layout.min.css"),
    "main_js": Bundle("js/main.js", filters=None, output="js/main.min.js"),
}

# Sources files or directory to synchronize within the static directory
FILES_TO_SYNC = (
    # Synchronize images if any
    "images",
)
