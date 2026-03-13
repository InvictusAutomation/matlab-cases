% 086_bisection
f=@(x) x^2-2; a=1; b=2; for i=1:50, m=(a+b)/2; if f(m)>0, b=m; else a=m; end; end