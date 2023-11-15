# SETUP

## Classic setup
check sourse
- $ which python
- .venv\Scripts\activate
- deactivate
- pip freeze > requirements.txt
- pip install -r .\requirements.txt


poetry
    python.exe -m pip install --upgrade pip
    pip install poetry
    poetry config --local virtualenvs.in-project true
    touch README.md
    poetry init -n
    poetry install


## poetry does not work with files whose encoding is not UTF-8 !!