# online_shop
A very small website for buying stuffs powered by django.
It does:
- adding and deleting products and different related categories by admin 
- user registerations
- making users' baskets to hold desired products
- ...

** payment gate is not connected to it **

usage - linux:

- install python, pip and virtualenv(wrapper)
- git clone https://github.com/SaEED-ABB/online_shop.git
- cd online_shop
- virtualenv -p python3 venv
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- // go to the link and see no products found
- python manage.py createsuperuser
- // go to the admin pannel and create some recursive categories and their related products and again see the Home page
- // signup some users and you can add products to your basket, see the basket content and leave comment for each product in each product detail page

