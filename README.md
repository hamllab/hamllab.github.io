# hamllab.github.io

Staging area for HaML Lab website.

## Installation

To make changes to the website from your machine, you must first set up your environment.

-   Install R, RStudio, and a recent version of Python.
-   Open RStudio and clone this repository.
-   Create a Python virtual environment under the repository directory using `python -m venv venv`. This only needs to be done once.
-   Activate the virtual environment using `. venv/bin/activate` and install the Python package using `pip install -e .` This only needs to be rerun if a new module has been added to the `haml` Python package.
-   Install the Python environment to Jupyter using `python -m ipykernel install --user --name hamllab`. This only needs to be done once.

Now restart RStudio. You should then be able to run `quarto render` from the Terminal tab or use the Render button on the editor window to generate the site. Look over the output carefully. If everything looks good, then run `quarto publish gh-pages`. See the [Quarto documentation](https://quarto.org/docs/publishing/github-pages.html) for details.

## Updating publications

To update the publication list, edit `papers.json` to add entries. Entries must be compatible with CSL. Special fields in each paper entry can be used to support specific features:

-   icon: Path to a PNG file that illustrates some key idea from the paper. Should only include black and transparency, so the icon will appear silhouetted against the background image, `images/logo_background.png`. The image must be 600x600. Resizing can be quickly done using ImageMagick. For example, `convert original_image.png -resize 600x600 resized_image.png`.
-   DOI: Should just include the DOI by itself, not the full URL. Adds a link to the paper entry.
-   link: Indicates a non-DOI persistent URL.
-   PMID: PubMed identifier, used to generate a link to the PubMed version of the article.
-   code: URL of code used in the paper.
-   data: URL of data used in the paper.
-   post: URL of a social media post about the paper.
-   preprint: URL of a preprint of the paper (for Submitted, In revision, and In press articles only).

Articles that have not yet been published can be included by setting the status property to "Submitted", "In revision", or "In press". These articles should only be included if there is a preprint. Indicate a URL to the preprint using the "preprint" property.
