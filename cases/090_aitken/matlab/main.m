% 090_aitken
g=@(x) (x+2/x)/2; x0=1; for i=1:5, x1=g(x0); x2=g(x1); x0=x0-(x1-x0)^2/(x2-2*x1+x0); end