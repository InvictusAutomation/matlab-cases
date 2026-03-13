% 065_ode45
f=@(t,y) y; [t,y]=ode45(f,[0 1],1)