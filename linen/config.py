import sys
from linen.util import checkpass

try:
    from linfile import *
except ImportError:
    sys.stderr.write('error in configuration file.')
    sys.stderr.write("do you have linfile.py in the root directory of your Django project?")
    sys.exit(1)

class LinenSettings(object):
    def __init__(self):
        self._eval_load_balancer()
        self._list_domains()
        self._list_SQL()
        self._list_static()
        self.USERS = USERS
        self._merge_passwords()
        self.REPO_URL = REPO['URL']
        self.REPO_BRANCH = REPO['BRANCH']
        self.PYTHON = PYTHON['VERSION']
        self.VIRTUALENV = PYTHON['VIRTUALENV']
        self.LOCALENV = PYTHON['LOCALENV']


    def _eval_load_balancer(self):
        """passing APACHE_HOSTS a list of length greater than one
        converts the first host to a load balancer"""
        if type(APACHE_HOSTS) is list:
            if len(APACHE_HOSTS) > 1:
                self.LOAD_BALANCER = APACHE_HOSTS.pop(0)
            self.APACHE_HOSTS = APACHE_HOSTS
        else:
            self.APACHE_HOSTS = list(APACHE_HOSTS)
            self.LOAD_BALANCER = None

    def _list_domains(self):
        """passing DOMAIN_NAMES a list of length greater than one
        converts the first host to the ServerName and the others 
        to ServerAlias"""
        if type(DOMAIN_NAMES) is not list:
            self.DOMAIN_NAMES = list(DOMAIN_NAMES)
        else:
            self.DOMAIN_NAMES = DOMAIN_NAMES

    def _list_SQL(self):
        if type(MYSQL_HOSTS) is not list:
            self.MYSQL_HOSTS = list(MYSQL_HOSTS)
        else:
            self.MYSQL_HOSTS = MYSQL_HOSTS

    def _list_static(self):
        if type(MEDIA_HOSTS) is not list:
            self.MEDIA_HOSTS = list(MEDIA_HOSTS)
        else:
            self.MEDIA_HOSTS = MEDIA_HOSTS

    def _merge_passwords(self):
        PASSWORDS = checkpass()
        self.USERS['SUPERUSER']['password'] = PASSWORDS['Django']
        self.USERS['MYSQL_INFO']['password'] = PASSWORDS['MySQL']

def __init__():
    pass    
