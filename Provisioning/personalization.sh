#!/bin/bash

####################################
# Personal Configuration Variables #
####################################
    git_user_email="thomas@potenza.me";
    git_user_name="TJ Potenza";

############################
# Fish, my shell of choice #
############################
    sudo apt-add-repository ppa:fish-shell/release-2 &&
    sudo apt-get update &&
    sudo apt-get install -y fish;

    rm -rf "$home/.config/fish" &&
    mkdir -p "$home/.config" &&
    git clone "https://github.com/tjpotenza/my-fish-config.git" "$home/.config/fish" &&
    sudo chsh -s $(which fish) $user;

#######################
# Git Config settings #
#######################
    git config --global user.email "$git_user_email";
    git config --global user.name "$git_user_name";
    git config --global push.default 'simple';
