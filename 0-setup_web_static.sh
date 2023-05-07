#!/usr/bin/env bash

# Install Nginx if it not already installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create the necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

# Create a fake HTML file
echo "Fake HTML file to test Nginx configuration" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/^\s*server\s*{/,/^\s*}\s*$/ s|^\(\s*\)#\?\(\s*root\s*/var/www/html;\)|\1alias /data/web_static/current/;|' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
