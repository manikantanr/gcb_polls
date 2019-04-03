import nox


@nox.session()
def codestyle(session):
    session.install('pycodestyle')
    session.run('pycodestyle', '--exclude', 'migrations,settings.py,.nox', '.')


@nox.session()
def isort(session):
    session.install('isort')
    session.run('isort', '--check-only', '--skip', 'polls/migrations/')


@nox.session()
def tests(session):
    session.install('-r', 'requirements.txt')
    session.run('python', 'manage.py', 'test')
