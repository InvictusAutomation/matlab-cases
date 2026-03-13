% 007_matrix_norm - 矩阵范数
% 计算矩阵的各种范数

%% 定义矩阵A
A = [1 2 3; 4 5 6; 7 8 9];

%% 计算范数
n1 = norm(A, 1);        % 1-范数（列范数）
n2 = norm(A, 2);        % 2-范数（谱范数）
nF = norm(A, 'fro');   % Frobenius范数
nInf = norm(A, inf);   % 无穷-范数（行范数）

disp('矩阵A:'); disp(A);
disp('1-范数:'); disp(n1);
disp('2-范数:'); disp(n2);
disp('F-范数:'); disp(nF);
disp('无穷-范数:'); disp(nInf);
