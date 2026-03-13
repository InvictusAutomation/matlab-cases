% 027_qr_solve
A=[1 2; 3 4]; b=[5;11]; [Q,R]=qr(A); x=R\(Q'*b)