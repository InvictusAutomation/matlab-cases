% 085_fixed_point
g=@(x) (x+2/x)/2; x=1; for i=1:10, x=g(x); end