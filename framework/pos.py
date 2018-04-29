from os import getcwd, chdir, environ
from subprocess import Popen, PIPE


class Pos(object):

	def __init__(self, user_class):
		self.user_class = user_class

	def clean_code(self):
		""" Method to clean the target code
		    This method uses methods defined by the user
		    It cleans all the executable files
		"""
		path = getcwd()
		clean_path = self.user_class.clean_path
		clean_command = self.user_class.clean_command 

		chdir(clean_path)

		my_env = environ.copy()
		my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
		process = Popen(clean_command, shell=True, stdout=PIPE)
		out, err =  process.communicate()
		chdir(path)
