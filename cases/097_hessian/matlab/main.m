% 097_hessian
f=@(x) x(1)^2+x(1)*x(2)+x(2)^2; hessian(f,[1,1])