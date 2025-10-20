#!/bin/bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
read -p "Press any key to continue..."
