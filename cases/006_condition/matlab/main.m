% Matrix Condition Number
A = [1 2; 3 4];
c = cond(A);
disp(['Condition: ', num2str(c)]);