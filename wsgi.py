# import sys
#
# project_home = 'D:/FTP/Слава/python/fleet/project_a_o_i_d/project'
# if project_home not in sys.path:
#     sys.path = [project_home] + sys.path

from project import create_app
application = create_app()

from waitress import serve
serve(application, host="192.168.1.59", port=10000)
