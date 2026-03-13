% 074_thin_plate
x=0:.25:1; y=x; [X,Y]=meshgrid(x,y); Z=sin(pi*X).*cos(pi*Y); tp=tpaps(x,y,Z);