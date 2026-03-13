% 093_central_diff
f=@(x) x^2; h=0.01; df=(f(1+h)-f(1-h))/(2*h)