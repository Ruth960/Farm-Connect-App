python -m venv env  ----Create virtual environment
source ../env/Scripts/activate   ---Activate virtual environment
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers ---install django and  other libraries

python manage.py runserver 0.0.0.0:8000  ---To start django environment
//when you add changes
python manage.py makemigrations
python manage.py migrate

