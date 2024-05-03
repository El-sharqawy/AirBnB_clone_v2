#!/usr/bin/env bash
# a Bash script that sets up our web servers for the deploments of web_static.

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

sudo sh -c 'echo -e "<!DOCTYPE html>\n<html>\n<body>\n<p>Hello World</p>\n</body>\n</html>" > data/web_static/releases/test/index.html'

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart
