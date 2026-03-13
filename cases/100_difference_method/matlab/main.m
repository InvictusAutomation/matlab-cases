% 100_difference_method
N=10; h=1/N; A=diag(2*ones(N-1,1))-diag(ones(N-2,1),1)-diag(ones(N-2,1),-1); A=A/h^2