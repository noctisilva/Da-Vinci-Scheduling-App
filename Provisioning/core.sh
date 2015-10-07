#!/bin/bash

###########################
# Configuration Variables #
###########################
    user="vagrant";
    group="vagrant";
    home="/home/$user";
    provisioning_root="/vagrant/Provisioning";

#####################
# General Utilities #
#####################
    # The obligatory apt-get update
    sudo apt-get update;

    # Git
    sudo apt-get install -y git;

    # Nodejs / NPM / Node Packages
    curl -sL https://deb.nodesource.com/setup | sudo bash - &&
    sudo apt-get install -y nodejs;
    sudo npm install -g bower;
    sudo npm install -g gulp;

    # Google Cloud SDK
    . "$provisioning_root/gcloud.sh";

#################
# PHP / Laravel #
#################
    # PHP itself
    sudo apt-get install -y php5-cli php5-cgi;
    sudo apt-get install -y php5-mcrypt && php5enmod mcrypt;

    # Composer (Package Manager)
    curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin/ --filename=composer;

    # Laravel CLI Installer
    /usr/local/bin/composer global require "laravel/installer=~1.1";

################################
# Non-Essential Customizations #
################################
    # Shell Customization and Such
    #. "$provisioning_root/personalization.sh";
