from controllers.controller import Controller

options = {
	"application": {
		"address": "127.0.0.1",
		"port": 8080
	},
	"urls": {
		"": Controller()
	},
	"views": {
		"templates_path": "views.templates"
	}
}

