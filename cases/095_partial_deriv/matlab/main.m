% 095_partial_deriv
f=@(x,y) x^2+y^2; h=0.01; dfdx=(f(1+h,1)-f(1-h,1))/(2*h)