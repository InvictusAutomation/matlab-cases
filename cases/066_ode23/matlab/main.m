% 066_ode23
f=@(t,y) y; [t,y]=ode23(f,[0 1],1)