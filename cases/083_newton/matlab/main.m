% 083_newton
f=@(x) x^2-2; df=@(x) 2*x; x=1; for i=1:10, x=x-f(x)/df(x); end