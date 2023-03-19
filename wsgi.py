from project import create_app
application = create_app()

from waitress import serve
serve(application, host="192.168.1.59", port=10000)
