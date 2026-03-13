% 063_boundary_value
y=bvp4c(@(x,y) [y(2); -y(1)],@(ya,yb) [ya(1)-1; yb(1)+1])