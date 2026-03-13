% 004_svd_decomposition - 奇异值分解SVD
% 将矩阵A分解为U*S*V'

%% 定义矩阵A
A = [1 2; 3 4; 5 6];

%% SVD分解
[U, S, V] = svd(A);

%% 显示结果
disp('原矩阵A:'); disp(A);
disp('左奇异向量U:'); disp(U);
disp('奇异值S:'); disp(S);
disp('右奇异向量V:'); disp(V);

%% 重构矩阵
A_reconstructed = U * S * V';
disp('重构矩阵:'); disp(A_reconstructed);
