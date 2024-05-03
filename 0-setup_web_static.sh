#!/usr/bin/env bash
# a Bash script that sets up our web servers for the deploments of web_static.

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo echo -e "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Hello World</p>
  </body>
</html>" | tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root   /var/www/html;
        index  index.html index.htm;

        location /hbnb_static {
                alias /data/web_static/current;
                index index.html index.htm;
        }

        error_page 404 /404.html;
        location /404 {
                root /var/www/html;
                internal;
        }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
