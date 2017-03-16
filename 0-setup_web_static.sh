#!/usr/bin/env bash
# Script taht sets up web servers to deploy AirBnB clone
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo -e '<!DOCTYPE html>\n<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' > /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu ~/data/
sudo sed -i "29i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
