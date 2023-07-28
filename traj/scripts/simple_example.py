import logging
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../src'))
from matplotlib import pyplot as plt
import traj


def test_zero_vel():
  '''始末速度为0的5种情况
  '''
  p_max=30
  v_max=3.0
  a_max=4.0
  j_max=10.0
  #case A1:  no limit is reached  
  traj.traj_plot.fit_and_plot_segment(0.0, 5.0,      0.0, 0.0,     p_max, v_max, a_max, 3.0)
  traj.traj_plot.fit_and_plot_segment(0.0, 1.0,      0.0, 0.0,     p_max, v_max, a_max, 3.0)
  traj.traj_plot.fit_and_plot_segment(0.0, 1.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)
  #case A2:  acc_limit is reached     
  traj.traj_plot.fit_and_plot_segment(0.0, 3.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)
  #case A3:  vel_limit and acc_limit are reached
  traj.traj_plot.fit_and_plot_segment(0.0, 5.0,      0.0, 0.0,     p_max, v_max, a_max, j_max)

def test_casea_duration():
  '''始末速度为0, case a的两种情况, 直接计算时间
  '''
  pmax=30
  acc_time=0.1
  vmax=3.0
  amax=vmax/acc_time
  jmax=vmax/acc_time/acc_time
  def duration(p):
    pos_min = 2.0*jmax*acc_time**3
    if p >= pos_min:
      return (p-pos_min)/vmax+acc_time*4
    else:
      return 4*(p/(2*jmax)) ** (1. / 3)
  logging.info(f'time={duration(1.0)}')
  traj.traj_plot.fit_and_plot_segment(0.0, 1.0,      0.0, 0.0,     pmax, vmax, amax, jmax)
  logging.info(f'time={duration(0.3)}')
  traj.traj_plot.fit_and_plot_segment(0.0, 0.3,      0.0, 0.0,     pmax, vmax, amax, jmax)
  
  


if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO, format="%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
  # test_zero_vel()
  test_casea_duration()
  
  