sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf ~/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -sf ~/web/etc/gunicorn.config   /etc/gunicorn.d/test
sudo ln -sf ~/web/etc/django.config    /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql restart
