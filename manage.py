from app import create_app, db
from flask_script import Manager, Shell, Server
from app.models import User

app = create_app('development')
app = create_app('test')

manager = Manager(app)
manager.add_command('server', Server)


@manager.add_command
def test():
    '''
    Function that runs the unit test
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=3).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)





if __name__ == '__main__':
    manager.run()