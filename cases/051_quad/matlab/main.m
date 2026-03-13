% 051_quad - 数值积分
% 使用quad函数进行数值积分

%% 定义被积函数
f = @(x) x.^2;

%% 数值积分
I = quad(f, 0, 1);  % ∫₀¹ x² dx = 1/3

%% 显示结果
fprintf('∫₀¹ x² dx = %f\n', I);
fprintf('精确值: %f\n', 1/3);
