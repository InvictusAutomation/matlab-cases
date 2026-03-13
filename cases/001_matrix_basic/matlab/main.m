% 001_matrix_basic - 矩阵基础运算
% 演示MATLAB中矩阵的创建、基本运算和操作

%% 1. 矩阵创建
A = [1 2 3; 4 5 6; 7 8 9];  % 3x3矩阵
B = eye(3);                   % 3x3单位矩阵
C = zeros(3, 3);              % 3x3零矩阵
D = ones(3, 3);               % 3x3全1矩阵
E = rand(3, 3);               % 3x3随机矩阵

%% 2. 矩阵运算
F = A + B;                    % 矩阵加法
G = A - B;                    % 矩阵减法
H = A * B;                    % 矩阵乘法
I = A .* B;                   % 元素乘法
J = A / B;                    % 矩阵右除
K = A \ B;                    % 矩阵左除

%% 3. 矩阵转置和逆
L = A';                        % 转置
M = inv(A);                    % 逆矩阵
N = pinv(A);                   % 伪逆

%% 4. 输出结果
disp('矩阵A:'); disp(A);
disp('矩阵B:'); disp(B);
disp('A+B:'); disp(F);
disp('A*B:'); disp(H);
disp('A的转置:'); disp(L);
