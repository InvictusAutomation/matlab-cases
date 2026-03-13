% 062_ode15s
f=@(t,y) -y; ode15s(f,[0 10],1)