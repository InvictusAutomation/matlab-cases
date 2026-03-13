% 005_eigen - 特征值与特征向量
% 计算矩阵的特征值和特征向量

%% 定义矩阵A
A = [4 2; 1 3];

%% 特征值分解
[V, D] = eig(A);

%% 显示结果
disp('矩阵A:'); disp(A);
disp('特征值:'); disp(D);
disp('特征向量矩阵V:'); disp(V);

%% 验证AV = VD
disp('验证AV=VD:'); disp(A*V - V*D);
