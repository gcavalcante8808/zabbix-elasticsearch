#!/bin/bash

GITHUB_RELEASE_VERSION=v0.7.2
GITHUB_USER=
GITHUB_TOKEN=
RELEASE=
REPO=
TAG=
NAME=
DESCRIPTION=

if [[ ! -f "github-release" ]]; then
    echo "Downloading github-release"
    wget -c https://github.com/aktau/github-release/releases/download/"${GITHUB_RELEASE_VERSION}"/linux-amd64-github-release.tar.bz2
    tar xvvf --strip 3 linux-amd64-github-release.tar.bz2
fi

echo "Creating desired Release"
github-release release \
   --user "${GITHUB_USER}" \
   --repo "${REPO}" \
   --tag "${TAG}" \
   --name "${NAME}" \
   --description "${DESCRIPTION}" \
   --pre-release

echo "Creating binaries from scripts"
for i in $(ls ../scripts/*.py); do 
    pyinstaller -F ../scripts/$i;
    rm *.spec 
done

echo "Creating scripts archive"
tar cjvf zbx-es-scripts.${TAG}.bz2 dist/*

echo "Sending the archive to Github Release Page"
github-release upload \
    --user aktau \
    --repo gofinance \
    --tag v0.1.0 \
    --name "gofinance-osx-amd64" \
    --file bin/darwin/amd64/gofinance

