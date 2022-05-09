isort .
black .
pylint $(git ls-files '*.py')
