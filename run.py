# this python script will run create the ui and control its flow.
from user_interface.helpers import csv_handling
from user_interface.views import connection_window
from user_interface.controllers import connection_controller
from user_interface.helpers import connection

connection_controller.show_window()
# print(connection.exec_query("SELECT airport_code FROM location"))
