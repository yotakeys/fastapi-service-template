#!/usr/bin/env bash

export PIPENV_VENV_IN_PROJECT=1
pipenv install
pipenv install --dev

if [ ! -f .env ]; then
    cp .env.example .env
fi