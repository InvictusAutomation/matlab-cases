% Eigenvalue Decomposition
A = [4 2; 1 3];
[V, D] = eig(A);
disp('Eigenvalues:'); disp(D);