import requests
import json
import os


host = "127.0.0.1:80"


def pretty(data):
	print("{")
	[print("\t", i, ":", data[i]) for i in data]
	print("}")


def make_call(headers, data, url, action):
	print("Data sent:")
	pretty(data)
	if action != "predict" and action != "test" and action != "train":
		r = requests.post(url = url, data = json.dumps(data), headers = headers)

	elif action == "predict":
		multipart_form_data = {'x_predict': open('x.csv', 'r')}
		r = requests.post(url = url, files=multipart_form_data, data=data, headers={"Authorization": headers["Authorization"]})

	elif action == "test":
		multipart_form_data = {'x_test': open('x.csv', 'r'), 'y_test': open('y.csv', 'r')}
		r = requests.post(url = url, files=multipart_form_data, data=data, headers={"Authorization": headers["Authorization"]})

	elif action == "train":
		multipart_form_data = {'x_train': open('x.csv', 'r'), 'y_train': open('y.csv', 'r')}
		r = requests.post(url = url, files=multipart_form_data, data=data, headers={"Authorization": headers["Authorization"]})

	print("Result:", r)
	pretty(r.json())


def read_test_data():
	f = open("test_data.md", 'r')
	tada = eval(f.read())
	f.close()
	return(tada)


def read_header_data():
	headers = {"content-type": "application/json"}
	try:
		f = open("header_data.md", "r")
		headers["Authorization"] = "token " + f.read().strip()
	except FileNotFoundError:
		x = input("Enrter Auth token: ").strip()
		f = open("header_data.md", "w")
		f.write(x)
		headers["Authorization"] = "token " + x
	f.close()
	return headers


def main():
	headers = read_header_data()
	tada = read_test_data()
	while 1:
		print("-" * os.get_terminal_size().columns)
		x = input("> ")
		if x == "help":
			print("List of commands")
			for i in tada:
				print(i)
			print("refresh data\nhelp\n^C")
			continue
		if x == "refresh data":
			tada = read_test_data()
			headers = read_header_data()
			print("Test cases and header refreshed")
			continue
		if x in tada:
			print("case:", x)
			make_call(headers, tada[x]["data"], "http://" + host + tada[x]["url"], x)
			print()
		else:
			print("Invalid action:", x)

try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print("Good Bye")
