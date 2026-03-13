% 087_nonlinear_system
f=@(x) [x(1)^2+x(2)^2-1; x(1)-x(2)]; fsolve(f,[1,1])