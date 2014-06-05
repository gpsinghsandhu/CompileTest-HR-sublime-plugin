import sublime
import sublime_plugin
import sys
import subprocess
import os
import threading

sys.path.append(os.path.join(os.path.dirname(__file__), "Markdow"))

class CompileTestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		comm = "compile_and_test.py source_file.cpp"
		#call(["python", comm])
		# retcode = subprocess.check_output(["python", comm], shell=True)
		# print(type(retcode))
		# print(str(retcode))
		# if retcode < 0:
		# 	print >>sys.stderr, "Child was terminated by signal", -retcode
		# else:
		# 	print >>sys.stderr, "Child returned", retcode
		#os.system("ls -l")
		print("\n\n\nRunning CompileTest Plugin...\n")
		script_path = os.path.join(os.path.dirname(__file__), "compile_and_test.py")
		#source_file_path = os.path.join(os.path.dirname(__file__), "source_file.cpp")
		source_file_path = self.view.file_name()
		if source_file_path is None:
			print("Please click inside the source_file and try again...\nexiting now")
			return
		print("Source File : " + self.view.file_name())
		#proc = subprocess.Popen(['python', script_path, source_file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		#proc = subprocess.Popen(['python', '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		thread = CompileThread(script_path, source_file_path)
		thread.start()



class CompileThread(threading.Thread):
	def __init__(self, script_path, file_path):
		self.script_path = script_path
		self.file_path = file_path
		self.result = None
		threading.Thread.__init__(self)

	def run(self):
		self.result = subprocess.Popen(['python', self.script_path, self.file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		print(self.result.communicate()[0].decode('utf-8'))
		return