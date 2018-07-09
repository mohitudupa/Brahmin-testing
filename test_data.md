{
	"get token": {
		"url": "/model/api/gettoken/",
		"auto": True,
		"data": {
					"username": "Your_user_name",
					"password": "Your_password",
		}
	},
	"change password": {
		"url": "/model/api/changepassword/",
		"auto": True,
		"data": {
					"old_password": "Old_password",
					"new_password": "New_password",
		}
	},
	"change token": {
		"url": "/model/api/changetoken/",
		"auto": True,
		"data": {
					"username": "Your_user_name",
					"password": "Your_password",
		}
	},
	"get details": {
		"url": "/model/api/getdetails/",
		"auto": True,
		"data": {
					"trash": False,
		}
	},
	"get names": {
		"url": "/model/api/getnames/",
		"auto": True,
		"data": {
					"trash": False,
		}
	},
	"get versions": {
		"url": "/model/api/getversions/",
		"auto": True,
		"data": {
					"name": "Iris Dataset",
					"trash": False
		}
	},
	"get instances": {
		"url": "/model/api/getinstances/",
		"auto": True,
		"data": {
					"name": "Iris Dataset",
					"version": "1.0",
					"trash": False
		}
	},
	"get model": {
		"url": "/model/api/getmodel/",
		"auto": True,
		"data": {
					"id": "5b3288e1da12b51608816dd5"
		}
	},
	"get log": {
		"url": "/model/api/getlog/",
		"auto": True,
		"data": {
					"id": "5b3288e1da12b51608816dd5"
		}
	},
	"get user log": {
		"auto": True,
		"url": "/model/api/getuserlog/",
		"data": {}
	},
	"get date log": {
		"auto": True,
		"url": "/model/api/getdatelog/",
		"data": {
					"date": "27-06-2018"
		}
	},
	"delete": {
		"auto": True,
		"url": "/model/api/delete/",
		"data": {
					"id": "5b3288e1da12b51608816dd5"
		}
	},
	"restore": {
		"auto": True,
		"url": "/model/api/restore/",
		"data": {
					"id": "5b3288e1da12b51608816dd5"
		}
	},
	"clone": {
		"auto": True,
		"url": "/model/api/clone/",
		"data": {
					"id": "5b3288e1da12b51608816dd5"
		}
	},
	"upload": {
		"auto": True,
		"url": "/model/api/upload/",
		"data": {
					"name": "Iris Dataset",
					"version": "1.0",
					"pickle" :"gANjc2tsZWFybi5saW5lYXJfbW9kZWwuYmFzZQpMaW5lYXJSZWdyZXNzaW9uCnEAKYFxAX1xAihYDQAAAGZpdF9pbnRlcmNlcHRxA4hYCQAAAG5vcm1hbGl6ZXEEiVgGAAAAY29weV9YcQWIWAYAAABuX2pvYnNxBkr/////WAUAAABjb2VmX3EHY251bXB5LmNvcmUubXVsdGlhcnJheQpfcmVjb25zdHJ1Y3QKcQhjbnVtcHkKbmRhcnJheQpxCUsAhXEKQwFicQuHcQxScQ0oSwFLBIVxDmNudW1weQpkdHlwZQpxD1gCAAAAZjhxEEsASwGHcRFScRIoSwNYAQAAADxxE05OTkr/////Sv////9LAHRxFGKJQyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHEVdHEWYlgJAAAAX3Jlc2lkdWVzcRdoCGgJSwCFcRhoC4dxGVJxGihLAUsAhXEbaBKJQwBxHHRxHWJYBQAAAHJhbmtfcR5LAFgJAAAAc2luZ3VsYXJfcR9oCGgJSwCFcSBoC4dxIVJxIihLAUsBhXEjaBKJQwgAAAAAAAAAAHEkdHElYlgKAAAAaW50ZXJjZXB0X3EmY251bXB5LmNvcmUubXVsdGlhcnJheQpzY2FsYXIKcSdoEkMIAAAAAAAA8D9xKIZxKVJxKlgQAAAAX3NrbGVhcm5fdmVyc2lvbnErWAYAAAAwLjE4LjJxLHViLg==",
					"private": True,
					"docs": "This is the first model upload"
		}
	},
	"update": {
		"auto": True,
		"url": "/model/api/update/",
		"data": {
					"id": "5b3288e1da12b51608816dd5",
					"new_name": "Iris test clone",
					"new_version": "2.0",
					"description": "Some update description",
					"new_private": True,
					"new_docs": "This is a clone of version 1.2"
		}
	},
	"commit": {
		"auto": False,
		"url": "/model/api/commit/",
		"data": {
					"id": "5b3288e1da12b51608816dd5",
					"description": "First commit",
		}
	},
	"discard": {
		"auto": True,
		"url": "/model/api/discard/",
		"data": {
					"id": "5b3288e1da12b51608816dd5"
		}
	},
	"get traceback": {
		"auto": True,
		"url": "/model/api/gettraceback/",
		"data": {
					"id": "5b3288e1da12b51608816dd5"
		}
	},
	"rollback": {
		"auto": True,
		"url": "/model/api/rollback/",
		"data": {
					"id": "5b3288e1da12b51608816dd5",
					"index": 0,
		}
	},
	"get status": {
		"auto": True,
		"url": "/model/api/getstatus/",
		"data": {
					"id": "5b3288e1da12b51608816dd5",
		}
	},
}
