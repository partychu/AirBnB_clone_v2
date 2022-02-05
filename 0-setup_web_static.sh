#!/usr/bin/env bash
# Set up webservers for deployment of web static
sudo apt update -y
sudo apt upgrade -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo touch index.html /data/web_static/releases/test/
sudo echo "Success {OK}" | sudo tee data/web_static/releases/test
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
