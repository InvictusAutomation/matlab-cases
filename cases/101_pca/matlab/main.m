% 101_pca - 主成分分析
% 使用MATLAB进行主成分分析

%% 生成样本数据
rng(42);
X = randn(100, 5) * 2 + ones(100, 5);

%% PCA分析
[coeff, score, latent] = pca(X);

%% 显示结果
disp('主成分系数:'); disp(coeff(:, 1:3));
disp('主成分得分:'); disp(score(1:5, :));
disp('方差解释比例:'); disp(latent / sum(latent) * 100);
