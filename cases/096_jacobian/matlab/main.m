% 096_jacobian
f=@(x) [x(1)^2; x(2)^2-x(1)]; jacobian(f,[1;1])