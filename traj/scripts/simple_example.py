import logging
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../src'))
from matplotlib import pyplot as plt
import traj

p_max=30
v_max=3.0
a_max=4.0
j_max=10.0

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO, format="%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
  #case A1:  no limit is reached  
  traj.traj_plot.fit_and_plot_segment(0.0, 5.0,      0.0, 0.0,     p_max, v_max, a_max, 3.0)
  traj.traj_plot.fit_and_plot_segment(0.0, 1.0,      0.0, 0.0,     p_max, v_max, a_max, 3.0)
  traj.traj_plot.fit_and_plot_segment(0.0, 1.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)
  #case A2:  acc_limit is reached     
  traj.traj_plot.fit_and_plot_segment(0.0, 3.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)
  #case A3:  vel_limit and acc_limit are reached
  traj.traj_plot.fit_and_plot_segment(0.0, 5.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)
  