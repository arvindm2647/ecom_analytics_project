#!/bin/bash
# Setup virtual env and run notebook (Linux / WSL)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
