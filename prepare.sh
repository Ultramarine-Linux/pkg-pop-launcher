#!/bin/bash
spectool -g pop-launcher.spec || true

FOLDER="$PWD"

# Extract the tarball to /tmp/src/
mkdir -p /tmp/src
tar -xzf ./*.tar.gz -C /tmp/src

pushd /tmp/src/* || exit

just vendor

mv -v ./vendor.tar "$FOLDER"/vendor.tar

popd || exit

rm -rf /tmp/src