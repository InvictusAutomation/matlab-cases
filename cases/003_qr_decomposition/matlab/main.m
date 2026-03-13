% 003_qr_decomposition - QR分解
% 将矩阵A分解为正交矩阵Q和上三角矩阵R

%% 定义矩阵A
A = [12 -51 4; 6 167 -68; -4 24 -41];

%% QR分解
[Q, R] = qr(A);

%% 显示结果
disp('原矩阵A:'); disp(A);
disp('正交矩阵Q:'); disp(Q);
disp('上三角矩阵R:'); disp(R);
disp('Q*R:'); disp(Q*R);

%% 验证Q的正交性
disp('Q''*Q (应为单位矩阵):'); disp(Q'*Q);
