% Matrix Norm
A = [1 2; 3 4];
n1 = norm(A, 1);
n2 = norm(A, 2);
nF = norm(A, 'fro');
disp([n1 n2 nF]);