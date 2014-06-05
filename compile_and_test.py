import requests
import json
import re
import sys
import time

# check if path to source file given
if(len(sys.argv) < 2):
	print("Usage : python compile_and_test <path/to/source/file>")
	exit()

# open source file
filename = str(sys.argv[1])
source_file = open(filename, 'r')

# extract url from file -- search for challenges/......>
code = source_file.read()

prob = re.search(r'url=[\'"]?([^\'" >]+)', code)
if not prob:
	print "cannot find url with \"url=\" phrase \nexiting now..."
	exit()

# create apt url
url = prob.group()
contests_index = url.find("contests")
if(contests_index != -1):
	url = url[contests_index:]
	url = "https://www.hackerrank.com/rest/" + url + "/compile_tests"
else:
	challenges_index = url.find("challenges")
	url = url[challenges_index:]
	url = "https://www.hackerrank.com/rest/contests/master/" + url + "/compile_tests"

#url = "https://www.hackerrank.com/rest/contests/master/" + prob.group() + "/compile_tests"

# print running info
print "url : " + url

# find extract extension -- searches for last '.'
index = filename.rfind('.')
if(index == -1):
	print "source file does not have a valid extenstion... \nexiting now..."
	exit()
extension = filename[index+1:]

# select language based on extension
language = ""
if extension == "cpp":
	language = "cpp"
elif extension == "c":
	language = "c"
elif extension == "py":
	language = "python"
elif extension == "java":
	language = "java"
else:
	print "source file does not have a valid extenstion... \nexiting now..."
	exit()


# make POST request with code and language
payload = {'code' : code, 'language' : language} 

parameters_json = json.dumps(payload)
headers = {'Content-Type': 'application/json'}
r = requests.post(url, data=parameters_json, headers=headers)

# if request fails exit
if not r:
	print "check problem url and your internet connection... \nexiting now..."
	exit()
# get request cookies
cookie = r.cookies
# convert to json object
json_data = json.loads(r.text)

# extract submission id and print it
id_ = json_data['model']['id']
print("Submission id : " + str(id_) + "\n")

# make GET requests to get results
ret = requests.get(url + "/" + str(id_), cookies=cookie)

json_ret = json.loads(ret.text)

# repeat requests while we don't get 'compilemessage' -- indicator of the result
trails = 6
while (json_ret['model'].get('compilemessage') is None) and (trails > 0):
	ret = requests.get(url + "/" + str(id_), cookies=cookie)
	#print(ret.text)
	json_ret = json.loads(ret.text)	
	trails = trails-1
	time.sleep(1)

# get final output
output = json_ret

#print(output)
# check if 'stdout' in response is None(i.e compilation error) or not(i.e successful compilation)
stdout = output['model']['stdout']
testcase_message = output['model']['testcase_message']
expected_output = output['model']['expected_output']
if(stdout == None):
	# print compile message in case of compilation error
	print(output['model']['compilemessage'])
else:
	# print output and testcase_message in case of successful compilation
	for i in range(0,len(stdout)):
		print("Your Output :")
		print(stdout[i].encode('utf-8'))
		print("Expected Output :")
		print(expected_output[i].encode('utf-8'))
		print("Result : " + testcase_message[i])
		print("\n")
		