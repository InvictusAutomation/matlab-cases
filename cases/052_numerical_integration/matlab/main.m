% 052_numerical_integration - 数值积分
% 使用quadl进行高精度数值积分

%% 定义被积函数
f = @(x) sin(x);

%% 数值积分
I = quadl(f, 0, pi);  % ∫₀^π sin(x) dx = 2

%% 显示结果
fprintf('∫₀^π sin(x) dx = %f\n', I);
fprintf('精确值: %f\n', 2);
