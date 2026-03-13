% 068_ode15i
f=@(t,y,yp) yp-y; ode15i(f,[0 1],0,1)