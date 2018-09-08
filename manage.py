from app import create_app,db
from flask_script import Manager, Shell, Server
from app.models import User
from flask_migrate import Migrate, MigrateCommand
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
pass_secure  = db.Column(db.String(255))

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)
# @manager.add_command
# def test():
#     '''
#     Function that runs the unittest
#     '''
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=3).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)




if __name__ == '__main__':
    # app.secret_key='foobar'
    manager.run()