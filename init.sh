sudo pip install --upgrade django
sudo /etc/init.d/mysql restart
sudo mysql -uroot -e  "CREATE DATABASE ask_data"
sudo mysql -uroot -e  "CREATE USER 'andrey'@'localhost' IDENTIFIED BY 'andrey'"
sudo mysql -uroot -e  "GRANT ALL PRIVILEGES ON * . * TO 'andrey'@'localhost'"
python ask/manage.py makemigrations
python ask/manage.py migrate

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/hello /etc/gunicorn.d/hello
sudo ln -sf /home/box/web/etc/ask /etc/gunicorn.d/ask

sudo /etc/init.d/gunicorn restart
