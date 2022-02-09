Provisioning for a new site
===========================

## Required Packages:

* nginx
* Python 3.6
* venv + pip
* git

eg, on Ubuntu:

    sudo apt install nginx, git, python3, python3-venv, python3-pip

## Nginx Virtual Host Config

* see nginx.template.conf
* replace DOMAIN with, e.g. staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g. staging.my-domain.com
