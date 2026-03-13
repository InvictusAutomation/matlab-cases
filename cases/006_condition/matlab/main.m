% 006_condition - 矩阵条件数
% 计算矩阵的条件数，衡量方程组解的稳定性

%% 定义矩阵A
A = [1 2 3; 4 5 6; 7 8 9];

%% 计算条件数
cond1 = cond(A, 1);    % 1-条件数
cond2 = cond(A, 2);    % 2-条件数
condF = cond(A, 'fro'); % F-条件数
condInf = cond(A, inf); % 无穷-条件数

disp('矩阵A:'); disp(A);
disp('1-条件数:'); disp(cond1);
disp('2-条件数:'); disp(cond2);
disp('F-条件数:'); disp(condF);
disp('无穷-条件数:'); disp(condInf);
