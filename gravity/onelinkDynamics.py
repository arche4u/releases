"""
# Created by rama krishna at 3/16/2023 and 9:09 PM

Feature: #Data fitting for single-joint robot
# Enter feature description here

Scenario: # when the robotic joint lifting against the gravity
# Enter steps here
"""
import math
from math import exp
import numpy as np
import matplotlib.pyplot as plt
import sys

import pandas as pd
from scipy import optimize

global friction_model

def onejoint_model(theta,system_paramters):
    position = np.array(theta, dtype=float)
    system_paramters =np.array(system_paramters,dtype=float)
    torque = np.array(system_paramters[0]*system_paramters[1]*system_paramters[2]*np.cos(position) * (1/system_paramters[3]))
    # torque =np.array(m* g* l* math.cos(theta),dtype = float)
    return torque
    # velocity = np.array(theta, dtype=float)
    # friction =np.array(velocity*2.55*system_paramters[1])
    # return friction


def residual(system_paramters,actual_torques,theta,model):
    output =actual_torques - model(theta,system_paramters)
    return output



## Other minimizers have to be explored
## Other modules like lmfit and tensor flow to be explored

################################################# SCIPY Least Squares algorithm ###########################################################


def lsq_fitting(obj_func,initial_parameters,model,torque,position,bounds_tuple):
    values = optimize.least_squares(obj_func, initial_parameters, jac='3-point', bounds=bounds_tuple, method='trf',
    ftol=1e-15, xtol=1e-15, gtol=1e-15, x_scale=1.0, loss='soft_l1', f_scale=1.0, diff_step=None, tr_solver=None, tr_options={}, jac_sparsity=None, max_nfev=None, verbose=2,
    args=(torque,position,model))

    return values

# thet_0 =0
# a1 =0.15
# a2=0.15
# f1=1.2
# f2=1.2
# theta = [0.1, 0.2, 0.3]

friction_model =onejoint_model
datastore= pd.read_csv("../resource/data2.csv")
pos_velocity =np.array(datastore.Velocity[datastore.Velocity > 0])
pos_torque = np.array(datastore.Torque[datastore.Torque > 0])
# print([pos_velocity,pos_torque])
intial_friction_para = [0.5,9.8,0.5,1.0]
bounds_pos = ([0.5,9.8,0.45,-1.0], [0.53,9.81,0.51,1.0])

system = [0.525, 9.8, 0.5,1.0]
theta_r=np.linspace(-90,90,100)
theta_rad =np.deg2rad(theta_r)

real_torque =[]
real_pos =[]

for i in theta_rad:
    out =onejoint_model(i,system)
    real_torque.append(out*1.0)
    real_pos.append(i)



result_pos = lsq_fitting(obj_func=residual, initial_parameters=intial_friction_para,
                         model=onejoint_model,
                         torque=real_torque,position=real_pos, bounds_tuple=bounds_pos)

plt.figure()
plt.plot(theta_rad,real_torque, "r")
plt.plot(theta_rad, friction_model(theta_rad, result_pos.x), "g")
plt.xlabel('angle')
plt.ylabel('Torque')
plt.title('Fitted Data ')
plt.grid()
plt.legend(["Actual Data", "Estimated"])
plt.show()
d =np.array([1,2,3])
# print("cos value is: ", np.cos(d))
print("The optimized paramters for positive: ", result_pos.x)
# [0.50208747 9.80014188 0.55022645 0.95676468]