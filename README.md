# DRF-example

mkdir backend
cd backend

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate 

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# create a project
django-admin startproject ecom
cd ecom
django-admin startapp home

