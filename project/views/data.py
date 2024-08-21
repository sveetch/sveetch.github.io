import json
from pathlib import Path

from optimus.pages.views import PageViewBase


class DataView(PageViewBase):
    """
    Sample of PageViewBase usage to build a JSON ressource without template view.
    """

    title = "Not used"
    destination = "endpoint.json"
    datas = ["sample.json"]

    def render(self, env):
        """
        Build a JSON using some data from a view data.

        Arguments:
            env (jinja2.Jinja2Environment): Jinja environment.

        Returns:
            string: Page content to write in destination file.
        """
        super().render(env)

        sample_path = Path(self.settings.DATAS_DIR) / "sample.json"
        sample = json.loads(sample_path.read_text())

        return json.dumps({
            "sample.json": "\n\n".join(sample["items"]),
        }, indent=4)
