import requests
import json
import os


host = "127.0.0.1:8000"

instance_id = 0

tada = {
	"get token": {
		"url": "/model/api/gettoken/",
		"data": {
					"username": str,
					"password": str,
		}
	},
	"change password": {
		"url": "/model/api/changepassword/",
		"data": {
					"old_password": str,
					"new_password": str,
		}
	},
	"change token": {
		"url": "/model/api/changetoken/",
		"data": {
					"username": str,
					"password": str,
		}
	},
	"get details": {
		"url": "/model/api/getdetails/",
		"data": {
					"trash": bool,
		}
	},
	"get names": {
		"url": "/model/api/getnames/",
		"data": {
					"trash": bool,
		}
	},
	"get versions": {
		"url": "/model/api/getversions/",
		"data": {
					"name": str,
					"trash": bool
		}
	},
	"get instances": {
		"url": "/model/api/getinstances/",
		"data": {
					"name": str,
					"version": str,
					"trash": bool
		}
	},
	"get model": {
		"url": "/model/api/getmodel/",
		"data": {
					"id": str
		}
	},
	"get log": {
		"url": "/model/api/getlog/",
		"data": {
					"id": str
		}
	},
	"get user log": {
		"url": "/model/api/getuserlog/",
		"data": {}
	},
	"get date log": {
		"url": "/model/api/getdatelog/",
		"data": {
					"date": str
		}
	},
	"delete": {
		"url": "/model/api/delete/",
		"data": {
					"id": str
		}
	},
	"restore": {
		"url": "/model/api/restore/",
		"data": {
					"id": str
		}
	},
	"clone": {
		"url": "/model/api/clone/",
		"data": {
					"id": str
		}
	},
	"upload": {
		"url": "/model/api/upload/",
		"data": {
					"name": str,
					"version": str,
					"pickle" : str,
					"private": bool,
					"docs": str
		}
	},
	"update": {
		"url": "/model/api/update/",
		"data": {
					"id": str,
					"new_name": str,
					"new_version": str,
					"description": str,
					"new_private": bool,
					"new_docs": str
		}
	},
	"commit": {
		"url": "/model/api/commit/",
		"data": {
					"id": str,
					"description": str,
		}
	},
	"discard": {
		"url": "/model/api/discard/",
		"data": {
					"id": str
		}
	},
	"get traceback": {
		"url": "/model/api/gettraceback/",
		"data": {
					"id": str
		}
	},
	"rollback": {
		"url": "/model/api/rollback/",
		"data": {
					"id": str,
					"index": str,
		}
	},
	"get status": {
		"url": "/model/api/getstatus/",
		"data": {
					"id": str,
		}
	},
}


ml = {
	"train": {
		"url": "/model/api/train/",
		"data": {
					"split": str,
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
	"cluster": {
		"url": "/model/api/cluster/",
		"data": {
					"x_cluster": "",
		}
	},
}


def login():
	global headers
	data = {}
	data["username"] = input("username (<class> 'str'): ")
	data["password"] = input("password (<class> 'str'): ")
	url = "http://" + host + "/model/api/gettoken/"
	r = requests.post(url=url, data=json.dumps(data), headers={"content-type": "application/json"})
	if str(r)[-5: -2] == "200":
		if "token" in dict(r.json()):
			f = open("header_data.md", "w")
			f.write(dict(r.json())["token"])
			f.close()
			return True
	print("error")
	return False



def read_header_data():
	headers = {"content-type": "application/json"}
	try:
		f = open("header_data.md", "r")
		headers["Authorization"] = "token " + f.read().strip()
		f.close()
	except FileNotFoundError:
		if not login():
			print("Invalid username or password.")
			exit()
		f = open("header_data.md", "r")
		headers["Authorization"] = "token " + f.read().strip()
		f.close()
	return headers


def get_instance_id():
	global instance_id
	if instance_id == 0:
		instance_id = input("instance ID (<class> 'str'): ")
	return(instance_id)


def change_model():
	global instance_id
	instance_id = input("instance ID (<class> 'str'): ")


def do_json_action(headers, keytype, url):
	data = {}

	for key in keytype.keys():
		if key == "id":
			data["id"] = get_instance_id()
		elif keytype[key] == bool:
			data[key] = eval(input(str(key) + " (" + str(keytype[key]) + ")" + ": "))
		else:
			data[key] = keytype[key](input(str(key) + " (" + str(keytype[key]) + ")" + ": "))

	print("Data sent:")
	print(json.dumps(data, indent=4, sort_keys=True))
	
	r = requests.post(url=url, data=json.dumps(data), headers=headers)
	
	print("Result:", str(r)[-5: -2])
	
	if str(r)[-5: -2] == "200":
		print(json.dumps(r.json(), indent=4, sort_keys=True))
	else:
		print("error")


def do_form_action(headers, keytype, url):

	data ={"id": get_instance_id()}

	files = {}
	file_data = {}

	for key in keytype.keys():
		if key == "split":
			data["split"] = int(input("split (<class> 'str'): "))
		else:
			file_name = input("Enter file for " + key + ": ")
			files[key] = open(file_name, "r")
			file_data[key] = str(files[key])

	print("Data sent:")
	print(json.dumps(data, indent=4, sort_keys=True))
	print("Files sent:")
	print(json.dumps(file_data, indent=4, sort_keys=True))
	r = requests.post(url=url, files=files, data=data, headers={"Authorization": headers["Authorization"]})
	
	print("Result:", str(r)[-5: -2])
	
	if str(r)[-5: -2] == "200":
		print(json.dumps(r.json(), indent=4, sort_keys=True))
	else:
		print("error")


def main():
	headers = read_header_data()
	global tada, ml
	while 1:
		print("-" * os.get_terminal_size().columns)
		x = input("> ")
		if x == "help":
			print("List of commands")
			print("change model")
			for i in tada:
				print(i)
			print("^C")
		elif x == "change model":
			change_model()
		elif x in tada:
			print("case:", x)
			do_json_action(headers, tada[x]["data"], "http://" + host + tada[x]["url"])
			print()
		elif x in ml:
			print("case:", x)
			do_form_action(headers, ml[x]["data"], "http://" + host + ml[x]["url"])
			print()
		else:
			print("Invalid action:", x)

try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print("Good Bye")
