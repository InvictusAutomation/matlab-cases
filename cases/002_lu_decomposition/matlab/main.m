% 002_lu_decomposition - LU分解
% 将方阵A分解为下三角矩阵L和上三角矩阵U

%% 定义矩阵A
A = [4 3 2; 2 3 4; 1 1 1];

%% LU分解
[L, U] = lu(A);

%% 显示结果
disp('原矩阵A:'); disp(A);
disp('下三角矩阵L:'); disp(L);
disp('上三角矩阵U:'); disp(U);
disp('L*U:'); disp(L*U);

%% 使用LU分解求解线性方程组Ax=b
b = [7; 6; 3];
y = L \ b;
x = U \ y;
disp('解向量x:'); disp(x);
