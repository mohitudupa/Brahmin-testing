import requests
import json
import os
# import gnureadline


host = "127.0.0.1:8000"

model_id = 0

template_id = 0

array = "array"

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
    
    "get model id": {
        "url": "/model/api/getmodelid/",
        "data": {
                    "name": str,
                    "version": str,
                    "trash": bool
        }
    },
    "get model": {
        "url": "/model/api/getmodel/",
        "data": {
                    "model_id": str
        }
    },
    "get log": {
        "url": "/model/api/getlog/",
        "data": {
                    "model_id": str
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
    "get traceback": {
        "url": "/model/api/gettraceback/",
        "data": {
                    "model_id": str
        }
    },
    "get status": {
        "url": "/model/api/getstatus/",
        "data": {
                    "model_id": str,
        }
    },
    "delete model": {
        "url": "/model/api/deletemodel/",
        "data": {
                    "model_id": str
        }
    },
    "restore model": {
        "url": "/model/api/restoremodel/",
        "data": {
                    "model_id": str
        }
    },
    "clone model": {
        "url": "/model/api/clonemodel/",
        "data": {
                    "model_id": str
        }
    },
    "upload model": {
        "url": "/model/api/uploadmodel/",
        "data": {
                    "name": str,
                    "version": str,
                    "pickle" : str,
                    "docs": str
        }
    },
    "edit model": {
        "url": "/model/api/editmodel/",
        "data": {
                    "model_id": str,
                    "new_name": str,
                    "new_version": str,
                    "description": str,
                    "new_docs": str
        }
    },
    "commit": {
        "url": "/model/api/commit/",
        "data": {
                    "model_id": str,
                    "description": str,
        }
    },
    "discard": {
        "url": "/model/api/discard/",
        "data": {
                    "model_id": str
        }
    },
    "rollback": {
        "url": "/model/api/rollback/",
        "data": {
                    "model_id": str,
                    "index": str,
        }
    },
    "abort": {
        "url": "/model/api/abort/",
        "data": {
                    "model_id": str,
        }
    },
    "get result": {
        "url": "/model/api/getresult/",
        "data": {
                    "model_id": str,
        }
    },
    "get attribute": {
        "url": "/model/api/getattribute/",
        "data": {
                    "model_id": str,
                    "attribute": str,
        }
    },
}

def pretty(data):
    map_json = json.dumps(data, indent=4, sort_keys=True)
    print(map_json)


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
    headers = {"Content-type": "application/json"}
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


def get_model_id():
    global model_id
    if model_id == 0:
        model_id = input("instance ID (<class> 'str'): ")
    return(model_id)


def get_template_id():
    global template_id
    if template_id == 0:
        template_id = input("template ID (<class> 'str'): ")
    return(template_id)


def change_model():
    global model_id
    model_id = input("instance ID (<class> 'str'): ")


def change_template():
    global template_id
    template_id = input("template ID (<class> 'str'): ")


def do_json_action(headers, keytype, url):
    data = {}

    for key in keytype.keys():
        if key == "model_id":
            data["model_id"] = get_model_id()
        elif key == "template_id":
            data["template_id"] = get_template_id()
        elif keytype[key] in [bool, dict]:
            data[key] = eval(input(str(key) + " (" + str(keytype[key]) + ")" + ": "))
        else:
            data[key] = keytype[key](input(str(key) + " (" + str(keytype[key]) + ")" + ": "))

    print("Data sent:")
    print(json.dumps(data, indent=4, sort_keys=True))
    # pretty(data)
    
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    
    print("Result:", str(r)[-5: -2])
    
    if str(r)[-5: -2] == "200":
        print(json.dumps(r.json(), indent=4, sort_keys=True))
        # pretty(r.json())
    else:
        print("error")


def do_form_action(headers, url):

    files = {}
    data = {}

    types = ["int", "str", "float", "bool"]

    data["type_data"] = eval(input("Enter the type list: <list> "))
    data["model_id"] = get_model_id()
    data["function"] = input("Enter the function name: <str> ")
    data["kwargs"] = eval(input("Enter the value for kwargs: <bool> "))

    for i in data["type_data"]:
        if i[1] in types:            
            data[i[0]] = eval(i[1])(input("Enter the value for " + i[0] + ": <" + i[1] + "> "))
        elif i[1] == "array":
            file_name = input("Enter the value for " + i[0] + ": <csv_file> ")
            files[i[0]] = open(file_name, "r")

    data["type_data"] = str(data["type_data"])
    print("Data sent:")
    print(json.dumps(data, indent=4, sort_keys=True))
    r = requests.post(url=url, files=files, data=data, headers={"Authorization": headers["Authorization"]})
    
    print("Result:", str(r)[-5: -2])
    
    if str(r)[-5: -2] == "200":
        print(json.dumps(r.json(), indent=4, sort_keys=True))
        # pretty(r.json())
    else:
        print("error")


def main():
    headers = read_header_data()
    global tada, ml
    while 1:
        print("-" * os.get_terminal_size().columns)
        x = input("> ")
        try:
            if x == "help":
                print("List of commands")
                print("change model")
                for i in tada:
                    print(i)
                print("^C")
            elif x == "change model":
                change_model()
            elif x == "change template":
                change_template()
            elif x in tada:
                print("case:", x)
                do_json_action(headers, tada[x]["data"], "http://" + host + tada[x]["url"])
                print()
            elif x == "exec command":
                print("case:", x)
                do_form_action(headers, "http://" + host + "/model/api/execcommand/")
                print()
            else:
                print("Invalid action:", x)
        except Exception as e:
            print(e)

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("Good Bye")
