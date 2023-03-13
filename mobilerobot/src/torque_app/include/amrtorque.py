"""
# Created by rama krishna at 3/8/2023 and 12:44 PM

Feature: #Enter feature name here
# Enter feature description here

Scenario: # Enter scenario name here
# Enter steps here
"""
import math
from PyQt5.QtWidgets import QMessageBox
import sys
from datetime import date, datetime, timedelta
import urllib.request as req

from UI.amr_troque import *


class MobileRobotTroque(Ui_MainWindow):

    def setupUi(self, MainWindow):

        super().setupUi(MainWindow)
        self.pushButton_calculate.clicked.connect(self.calculate)
           

    def calculate(self):
        g = 9.81
        # self.acc = 0.25
        wheel_diamter = 0.00
        numWheel = 0
        numWheel =int(self.lineEdit_noOfWheels.text())
        wheel_diamter = float(self.lineEdit_wheelDia.text())
        payload = float(self.lineEdit_payload.text())
        angle =float(self.lineEdit_slope.text())
        angle =angle*math.pi/180
        voltage = float(self.lineEdit_voltage.text())
        accel =float(self.lineEdit_robotReqAccel.text())
        eff =1.0
        friction_coeff = 1.0
        r = float(wheel_diamter/2)
        # Meter per Sec

        maxspeed = float(self.lineEdit_robotReqSpeed.text())
        #IN RPM
        motor_speed = maxspeed/(2*math.pi*(wheel_diamter/2) )

        f_g =payload*g # m.g

        grad_force =f_g*math.sin(angle)
        roll_force = friction_coeff*f_g*math.cos(angle)
        mass_force = payload*accel

        total_force = grad_force + roll_force + mass_force
        total_force_str = str(total_force)
        self.lineEdit_totalReqForce.setText(total_force_str)



        req_motor_force = total_force / (numWheel * eff)

        motor_torque = req_motor_force*r
        motor_torque_str =str(motor_torque)
        self.lineEdit_motorReqTroque.setText(motor_torque_str)

        req_motor_speed = (maxspeed/r) #*(60/2*math.pi) # V =W.r
        req_motor_speed_str = str(req_motor_speed)
        self.lineEdit_motorReqSpeed.setText(req_motor_speed_str)

        tor_motor = (1/numWheel)*(wheel_diamter/2)*total_force
        powOnMotor = total_force * voltage/(numWheel)

        power_motor = motor_torque*req_motor_speed
        self.lineEdit_motorPower.setText(str(power_motor))
        motor_current =power_motor/voltage
        self.lineEdit_motorCurrent.setText(str(motor_current))



        ##Testing
        # print(wheel_diamter)




    # def validInput(self,num):
    #
    #     if num.isnumeric()==True:
    #         return True
    #     else:
    #         return False
