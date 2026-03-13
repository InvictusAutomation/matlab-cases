% 084_secant
f=@(x) x^2-2; x0=1; x1=2; for i=1:10, x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0)); x0=x1; x1=x2; end