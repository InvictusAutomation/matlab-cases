% 079_nonlinear_fit
x=0:0.1:1; y=exp(-x)+0.1*randn(size(x)); fit=fit(x','y','exp1')