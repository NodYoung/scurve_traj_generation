#!/usr/bin/env python
"""
Simple example that fits general trajectory segment, given the start and
end positions/velocities. Start and end acceleration/jerk are assumed to be zero.
"""
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../src'))
from matplotlib import pyplot as plt
import traj

p_max=30
v_max=3.0
a_max=4.0
j_max=10.0   


############### CASE A: v_start = v_end = 0    [normal case, start and end velocities are zeros]
#case A1:  no limit is reached     
traj.traj_plot.fit_and_plot_segment(0.0, 1.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)
    
#case A2:  acc_limit is reached     
traj.traj_plot.fit_and_plot_segment(0.0, 3.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)      
    
#case A3:  vel_limit and acc_limit are reached    
traj.traj_plot.fit_and_plot_segment(0.0, 5.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)        
    

############## CASE B: v_start = v_end !=0   [ start and end velocities are equal but not null]
#case B1:  no limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, 2.0,      1.0, 1.0,     p_max, v_max, a_max, j_max)
       
#case B2:  vel_limit is reached 
traj.traj_plot.fit_and_plot_segment(0.0, 3.0,      2.5, 2.5,     p_max, v_max, a_max, j_max)   
   
#case B3:  acc_limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, 3.0,      0.5, 0.5,     p_max, v_max, a_max, j_max)           
   
#case B4:  vel_limit and acc_limit are reached   
traj.traj_plot.fit_and_plot_segment(0.0, 10.0,     0.5, 0.5,     p_max, v_max, a_max, j_max)    
   


############## CASE C:  v_start < v_end [acceleration]
#case C1:  no limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, 2.0,       0.5, 1.5,    p_max, v_max, a_max, j_max)    
    
##case C2:  vel_limit is reached 
traj.traj_plot.fit_and_plot_segment(0.0, 5.0,      2.0, 2.5,     p_max, v_max, a_max, j_max)    
    
##case C3:  acc_limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, 3.0,      0.5, 2.5,     p_max, v_max, a_max, j_max) 
    
##case C4:  vel_limit and acc_limit are reached   
traj.traj_plot.fit_and_plot_segment(0.0, 5.0,       0.5, 2.5,    p_max, v_max, a_max, j_max)    
   
   
   
############## CASE D:  v_start > v_end [deceleration]
#case D1:  no limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, 2.0,       1.5, 0.5,    p_max, v_max, a_max, j_max)     
    
##case D2:  vel_limit is reached 
traj.traj_plot.fit_and_plot_segment(0.0, 5.0,       2.5, 2.0,    p_max, v_max, a_max, j_max)        
    
##case D3:  acc_limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, 3.0,       2.5, 0.5,    p_max, v_max, a_max, j_max)
    
##case D4:  vel_limit and acc_limit are reached   
traj.traj_plot.fit_and_plot_segment(0.0, 5.0,       2.5, 0.5,    p_max, v_max, a_max, j_max)        
    
  


############### CASE A-: v_start = v_end = 0    [normal case, negative motion]
#case A1-:  no limit is reached     
traj.traj_plot.fit_and_plot_segment(0.0, -1.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)      
    
#case A2-:  acc_limit is reached     
traj.traj_plot.fit_and_plot_segment(0.0, -3.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)      
    
#case A3-:  vel_limit and acc_limit are reached    
traj.traj_plot.fit_and_plot_segment(0.0, -5.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)        
    

############## CASE B-: v_start = v_end !=0   [ start and end velocities are equal but not null]
#case B1-:  no limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, -2.0,      -1.0, -1.0,     p_max, v_max, a_max, j_max)
       
#case B2-:  vel_limit is reached 
traj.traj_plot.fit_and_plot_segment(0.0, -3.0,     -2.5, -2.5,     p_max, v_max, a_max, j_max)   
   
#case B3-:  acc_limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, -3.0,      -0.5, -0.5,     p_max, v_max, a_max, j_max)           
   
#case B4-:  vel_limit and acc_limit are reached   
traj.traj_plot.fit_and_plot_segment(0.0, -10.0,     -0.5, -0.5,     p_max, v_max, a_max, j_max)    
   

############## CASE C-:  v_start < v_end [acceleration]
#case C1-:  no limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, -2.0,       -0.5, -1.5,    p_max, v_max, a_max, j_max)    
    
##case C2-:  vel_limit is reached 
traj.traj_plot.fit_and_plot_segment(0.0, -5.0,      -2.0, -2.5,     p_max, v_max, a_max, j_max)    
    
##case C3-:  acc_limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, -3.0,      -0.5, -2.5,     p_max, v_max, a_max, j_max) 
    
##case C4-:  vel_limit and acc_limit are reached   
traj.traj_plot.fit_and_plot_segment(0.0, -5.0,       -0.5, -2.5,    p_max, v_max, a_max, j_max)    
   

############## CASE D-:  v_start > v_end [deceleration]
#case D1:  no limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, -2.0,       -1.5, -0.5,    p_max, v_max, a_max, j_max)     
    
##case D2:  vel_limit is reached 
traj.traj_plot.fit_and_plot_segment(0.0, -5.0,       -2.5, -2.0,    p_max, v_max, a_max, j_max)        
    
##case D3:  acc_limit is reached
traj.traj_plot.fit_and_plot_segment(0.0, -3.0,       -2.5, -0.5,    p_max, v_max, a_max, j_max)
    
##case D4:  vel_limit and acc_limit are reached   
traj.traj_plot.fit_and_plot_segment(0.0, -5.0,       -2.5, -0.5,    p_max, v_max, a_max, j_max)        
   



###############################################################################################
################ complex motion: v_start*v_end <0, +ve and -ve parts ##########################
###############################################################################################


############ CASE X: positive dominant motion: pos_diff > 0
### starting from +ve to -ve
traj.traj_plot.fit_and_plot_segment(0.0, 8.0,      1.5, -1.0,     p_max, v_max, a_max, j_max)   
### starting from -ve to +ve
traj.traj_plot.fit_and_plot_segment(0.0, 5.0,      -1.5, +1.0,     p_max, v_max, a_max, j_max)   


#############CASE Y: negative dominant motion: pos_diff < 0
### starting from +ve to -ve
traj.traj_plot.fit_and_plot_segment(0.0, -8.0,      1.5, -1.0,     p_max, v_max, a_max, j_max)   
### starting from -ve to +ve
traj.traj_plot.fit_and_plot_segment(0.0, -5.0,      -1.5, +1.0,     p_max, v_max, a_max, j_max)   
  