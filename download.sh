#!/bin/bash

set -e

VERSION=0.6.3

#wget https://github.com/kevinkreiser/prime_server/archive/$VERSION.tar.gz
#tar xvf $VERSION.tar.gz

git clone https://github.com/kevinkreiser/prime_server.git
cd prime_server
git submodule update --init --recursive

git checkout $VERSION
