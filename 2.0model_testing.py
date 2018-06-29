import requests
import json
import os


host = "127.0.0.1:8000"


instance_id = 0

ml = {
	"train": {
		"url": "/model/api/train/",
		"data": {
					"x_train": "",
					"y_train": "",
		}
	},
	"test": {
		"url": "/model/api/test/",
		"data": {
					"x_test": "",
					"y_test": "",
		}
	},
	"predict": {
		"url": "/model/api/predict/",
		"data": {
					"x_predict": "",
		}
	},
}

def pretty(data):
	print("{")
	[print("\t", i, ":", data[i]) for i in data]
	print("}")


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


def get_instance_id():
	global instance_id
	if instance_id == 0:
		instance_id = input("Enter the instance ID: ")
	return(instance_id)


def change_model():
	global instance_id
	instance_id = input("Enter the instance ID: ")

def do_json_action(headers, tada, url, action):
	data = {}
	if tada[action]["auto"]:
		data = tada[action]["data"]
		if "id" in tada[action]["data"]:
			data["id"] = get_instance_id()
	else:
		for key in tada[action]["data"].keys():
			data[key] = get_instance_id() if key == "id" else str(input("Enter " + key + ": "))

	print("Data sent:")
	pretty(data)
	
	r = requests.post(url=url, data=json.dumps(data), headers=headers)
	
	print("Result:", str(r)[-5: -2])
	
	if str(r)[-5: -2] == "200":
		pretty(r.json())
	else:
		print("error")


def do_form_action(headers, ml, url, action):

	data ={"id": get_instance_id()}

	files = {}

	for key in ml[action]["data"].keys():
		file_name = input("Enter file for " + key + ": ")
		files[key] = open(file_name, "r")

	if action == "train":
		data["split"] = int(input("Enter the split precentage: "))

	print("Data sent:")
	pretty(data)
	print(type(data["split"]))	
	r = requests.post(url=url, files=files, data=data, headers={"Authorization": headers["Authorization"]})
	
	print("Result:", str(r)[-5: -2])
	
	if str(r)[-5: -2] == "200":
		pretty(r.json())
	else:
		print("error")


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
		elif x == "refresh data":
			tada = read_test_data()
			headers = read_header_data()
			print("Test cases and header refreshed")
		elif x == "change model":
			change_model()
		elif x in tada:
			print("case:", x)
			do_json_action(headers, tada, "http://" + host + tada[x]["url"], x)
			print()
		elif x in ml:
			print("case:", x)
			do_form_action(headers, ml, "http://" + host + ml[x]["url"], x)
			print()
		else:
			print("Invalid action:", x)

try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print("Good Bye")
