% 151_fft - 快速傅里叶变换
% 使用FFT进行频谱分析

%% 生成信号
Fs = 1000;                    % 采样频率
t = 0:1/Fs:1-1/Fs;            % 时间向量
f1 = 50; f2 = 120;            % 信号频率
x = sin(2*pi*f1*t) + 0.5*sin(2*pi*f2*t);

%% FFT变换
N = length(x);
Y = fft(x);
P2 = abs(Y/N);
P1 = P2(1:N/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(N/2))/N;

%% 绘制频谱
plot(f, P1);
xlabel('频率 (Hz)');
ylabel('幅值');
title('信号频谱');
