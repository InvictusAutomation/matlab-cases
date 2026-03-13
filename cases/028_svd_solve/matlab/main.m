% 028_svd_solve
A=[1 2; 3 4]; b=[5;11]; [U,S,V]=svd(A); x=V*(S\(U'*b))