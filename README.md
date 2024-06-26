# hamllab.github.io

Staging area for HaML Lab website.

## Routine updates

The website can be updated by making edits directly on GitHub. First, create a branch to work from; give it a name that indicates what you will be adding. Next, make edits in that branch. When you have draft edits, create a pull request to merge your branch into the "main" branch. This will trigger rendering of the new version of the website. See the Firebase console for a link, or look in the GitHub Actions tab; that will show the link in the output of the job. If the draft rendered website looks good, merge the pull request. This will trigger rendering and deployment to the main live website at https://hamllab.org.

## Local installation

A local setup can make it easier to test out large changes to the website. To make changes to the website from your machine, you must first set up your environment.

-   Install R, RStudio, and a recent version of Python.
-   Open RStudio and clone this repository. Create a new branch if necessary and checkout that branch.
-   Create a Python virtual environment under the repository directory using `python -m venv venv`. This only needs to be done once.
-   Activate the virtual environment using `. venv/bin/activate` and install the Python package using `pip install -e .` This only needs to be rerun if a new module has been added to the `haml` Python package.
-   Install the Python environment to Jupyter using `python -m ipykernel install --user --name hamllab`. This only needs to be done once.

Now restart RStudio. You should then be able to run `quarto render` from the Terminal tab or use the Render button on the editor window to generate the site. When your edits are drafted, push the changes from your branch to the website repository. See above for details about checking the draft changes and publishing them.

See the [Quarto documentation](https://quarto.org/docs/publishing/github-pages.html) for details.

## Updating website pages

See the [HaML Lab Wiki](https://wiki.hamllab.org/en/role/website-admin) for instructions on updating the different pages of the website.
