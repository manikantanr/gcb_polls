# Google cloud build CI/CD with Django Poll App


## Usage

### Install application dependencies
```
pip install -r requirements.txt
```

### Check code style
```
pycodestyle --exclude migrations,settings.py,.nox .
```

### Check import styles
```
isort --check-only --skip polls/migrations/
```

### Run tests manually.
```
python  manage.py test
```

## Using Nox

### Install nox

```
pip install -U nox
```

### Run nox


```
nox
```