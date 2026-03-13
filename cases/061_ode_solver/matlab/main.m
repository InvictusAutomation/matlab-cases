% 061_ode_solver
f=@(t,y) -y; [t,y]=ode45(f,[0 10],1)