#!/usr/local/bin/bash
celery flower -A {{cookiecutter.project_slug}} --address=127.0.0.1 --port=5555