"""
This script runs the Ncuhome_HackFeb_QAndA_Rebuild application.
"""

from flask_script import Manager, Shell
from app import create_app
import os

env = os.getenv('FLASK_CONFIG') or 'dev'
app, db = create_app(env)

manager = Manager(app)

def make_shell_context():
    return {'app': app, 'db': db}

manager.add_command('shell', Shell(make_context = make_shell_context))

if __name__ == '__main__':
    print('Current config is:', env)
    manager.run()
