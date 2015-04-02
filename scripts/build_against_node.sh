#!/usr/bin/env bash

set -u -e

function publish() {
    node-pre-gyp publish
    node-pre-gyp info
    node-pre-gyp clean
    make clean
    # now install from binary
    INSTALL_RESULT=$(npm install --fallback-to-build=false > /dev/null)$? || true
    # if install returned non zero (errored) then we first unpublish and then call false so travis will bail at this line
    if [[ $INSTALL_RESULT != 0 ]]; then echo "returned $INSTALL_RESULT";node-pre-gyp unpublish;false; fi
    # If success then we arrive here so lets clean up
    node-pre-gyp clean
}

if [[ ! -d ../.nvm ]]; then
    git clone https://github.com/creationix/nvm.git ../.nvm
fi

set +u
source ../.nvm/nvm.sh
nvm install $NODE_VERSION
nvm use $NODE_VERSION
set -u

publish