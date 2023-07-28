import logging
import numpy as np
import sympy as sp

def s_curve():
  p0, v0, a0 = sp.symbols('p0, v0, a0')
  t, ta, tv = sp.symbols('t, ta, tv')
  jm = sp.symbols('jm')
  a1 =  jm*t +  a0
  a2 =          a1
  a3 = -jm*t +  a2
  a4 =          a3
  a5 = -jm*t +  a4
  a6 =          a5
  
  v1 =  jm*t*t/2.0 +  a0*t   + v0
  v2 =                a1*ta  + v1
  v3 = -jm*t*t/2.0 +  a2*t   + v2
  v4 =                a3*tv  + v3
  v5 = -jm*t*t/2.0 +  a4*t   + v4
  v6 =                a5*ta  + v5

  p1 =  jm*t*t*t/6.0 +  a0*t*t/2.0    + v0*t  + p0
  p2 =                  a1*ta*ta/2.0  + v1*ta + p1
  p3 = -jm*t*t*t/6.0 +  a2*t*t/2.0    + v2*t  + p2
  p4 =                  a3*t*t/2.0    + v3*tv + p3
  p5 = -jm*t*t*t/6.0 +  a4*t*t/2.0    + v4*t  + p4
  p6 =                  a5*ta*ta/2.0  + v5*ta + p5
  p7 =  jm*t*t*t/6.0 +  a6*t*t/2.0    + v6*t  + p6
  logging.info(sp.simplify(p7.subs([(ta, 0), (tv, 0), (p0, 0), (v0, 0), (a0, 0)])))
  

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
  s_curve()