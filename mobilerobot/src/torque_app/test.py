"""
# Created by rama krishna at 3/8/2023 and 9:31 PM

Feature: #Enter feature name here
# Enter feature description here

Scenario: # Enter scenario name here
# Enter steps here
"""
from PyQt5.QtWidgets import QMessageBox
import sys
from datetime import date, datetime, timedelta
import urllib.request as req


def license():
    CONST = 2 * 3.1416 * 1000

    # online check
    data = []
    with  req.urlopen('http://just-the-time.appspot.com/') as response:
        data = response.read()

    temp = str(data)
    year = temp[2:6]
    month = temp[7:9]
    date = temp[10:12]
    # offline check
    # dd/mm/YY H:M:S
    # now = datetime.now()
    # dt_string = now.strftime("%d%m%y")
    # dat = now.strftime("%d")
    # mon = now.strftime("%m")
    # yr = now.strftime("%Y")

    encryption_online = int( (int(month) * CONST) + (int(year) * CONST))
    encryption_online = str(encryption_online)

    encryption_offline = int((int(1) * CONST) + (int(year) * CONST))
    encryption_offline = str(encryption_offline)

    # Testing
    print("the online", encryption_online)
    print("the offline", encryption_offline)
    # if encryption_online >= encryption_offline:
    #     msg = QMessageBox()
    #     msg.setWindowTitle("ERROR")
    #     msg.setText("Please update the system's date&time part!")
    #     x = msg.exec_()  # this will show our messagebox
    #     sys.exit()

    if encryption_online <= encryption_offline:
        val_pass = True
        return val_pass
    else:

        msg = QMessageBox()
        msg.setWindowTitle("License Tool")
        msg.setText("Please update the license part!")
        x = msg.exec_()  # this will show our messagebox
        sys.exit()
        val_pass2 = False
        return val_pass2
val =license()
print(val)