#Git settings
git --global user.email "lyotchik1@mail.ru"
git --global user.name "pposad"

#Install packages
sudo apt-get install tree
sudo apt-get install htop
sudo apt-get install python-django-south
sudo pip install django-autofixture

#Change config
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf ~/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -sf ~/web/etc/gunicorn.config   /etc/gunicorn.d/test
sudo ln -sf ~/web/etc/django.config    /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart

#DateBase
sudo /etc/init.d/mysql restart

sudo mysql -uroot < ~/web/init_db
sudo python ~web/ask/manage.py syncdb
