CompileTest Plugin - CompileTest.py
-----------------------------------

Description
-----------
This sublime plugin can be used to directily compile and test your source code for problems at www.hackerrank.com. This plugin does not submits the code, instead it just execute "compile and test" available at www.hackerrank.com and outputs the response from the server. This plugin is actually a wrapper for another python script that I created which essentially(see compile_and_test.py below) does the same work.

Important - 1) your source file should have proper extensions :
				language  |  extension
				python    |  .py
				cpp       |  .cpp
				c         |  .c
				java      | .java
			2) you should mention correct url for the problem you are submitting the code
				e.g
				for this problem at :
				https://www.hackerrank.com/challenges/pairs

				your source file should contain (anywhere in the comments)

				<url=https://www.hackerrank.com/challenges/pairs>

				for a .cpp file it can be like this
				// <url=https://www.hackerrank.com/challenges/pairs>
				
Sublime
--------
sublime-text-3


Installation
------------
Just copy the entire folder to your sublime Packages folder. In ubuntu 12.04 it is like
/home/[username]/.config/sublime-text-3/Packages/


Usage
-----
To see output press ctrl+~
1) via text_commands 
    type in the command box (at bottom)
    'view.run_command('compile_test')'
    without qoutes
2) via menu
    Tools->CompileTest
3) via key bindings
    press f5
    
    you can change key-binding by modifying key value in 'Default (Linux).sublime-keymap' to something else

Output
------
see compile_and_test.py output below

Dependencies
------------
see dependencies for compile_and_test.py


------------------------------------------------------------------------------------------------------------------------------------------

compile_and_test.py
-------------------

Description
-----------

This is a simple python script to compile and test your soruce code for any problem at www.hackerrank.com. This sript does not submits your source_code, instead it simply does the "compile & test" (for details refer www.hackerrank.com) and outputs the response from www.hackerrank.com. This script takes as input - path/to/your/source/file and outputs response. Currently it only works for 4 languages i.e c, cpp, java, python

Important - 1) your source file should have proper extensions :
				language  |  extension
				python    |  .py
				cpp       |  .cpp
				c         |  .c
				java      |  .java
			2) you should mention correct url for the problem you are submitting the code
				e.g
				for this problem at :
				https://www.hackerrank.com/challenges/pairs

				your source file should contain (anywhere in the comments)

				<url=https://www.hackerrank.com/challenges/pairs>

				for a .cpp file it can be like this
				// <url=https://www.hackerrank.com/challenges/pairs>


Usage
-----

python compile_and_test.py /path/to/source/file

e.g

python compile_and_test.py /home/guru/source.cpp

Output
------

1) Succesfull compilation :
	Its outputs result in the following format:
	---------------------------------------------
	Your Output :
	.
	your output
	.
	.
	Expected Output :
	.
	expected output
	.
	.
	Result :
	result 
	-----------------------------------------------
	Result can either be "Success" or "Wrong Answer"
	
2) Unsuccessful compilation :
	compilation message

Platform
--------------

This script has been created and tested in Python version - 2.7.3 on Ubuntu 12.04

Dependencies
------------
This script requires 'requests' as a module. Please refer following url for details regarding installation:

http://docs.python-requests.org/en/latest/user/install/



