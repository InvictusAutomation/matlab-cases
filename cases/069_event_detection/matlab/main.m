% 069_event_detection
options=odeset('Events',@(t,y) y-2); ode45(@(t,y) -y,[0 5],1,options)