#!/bin/bash
#
#  Install dependencies for rendering the HaML Lab website.

python -m venv venv
. venv/bin/activate
pip install .
python -m ipykernel install --user --name hamllab
