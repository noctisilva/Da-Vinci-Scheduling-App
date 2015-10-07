#!/bin/bash

# Credit to the author of the following for the silent installation
# options for the sdk, much more convenient than my hacky solution
# with expect!
#
#   https://github.com/laander/vagrant-gcloud
(
    # Get and unpack the SDK
    cd /home/vagrant &&
    wget -q https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz &&
    tar xzvpf google-cloud-sdk.tar.gz &&
    rm google-cloud-sdk.tar.gz;

    # Install the SDK itself
    $HOME/google-cloud-sdk/install.sh --rc-path=$HOME/.bashrc --bash-completion=true --path-update=true --disable-installation-options;

    # Install the Python/PHP component
    $HOME/google-cloud-sdk/bin/gcloud components update app-engine-python;
)