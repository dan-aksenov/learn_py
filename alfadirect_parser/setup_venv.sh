#!/bin/bash
#

REPO_ROOT="`dirname \"$0\"`"

rm -rf $REPO_ROOT/venv
python3 -m venv $REPO_ROOT/venv

. $REPO_ROOT/venv/bin/activate

echo "Установка python-зависимости для ansible"
pip3 install -r $REPO_ROOT/requirements.txt --force
