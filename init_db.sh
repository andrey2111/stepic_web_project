sudo mysql -uroot -pandrey -e  "CREATE DATABASE ask_data"
sudo mysql -uroot -pandrey -e  "CREATE USER 'andrey'@'localhost' IDENTIFIED BY 'andrey'"
sudo mysql -uroot -pandrey -e  "GRANT ALL PRIVILEGES ON * . * TO 'andrey'@'localhost'"
