import time
import stddraw
import math

time_aggregate = time.localtime()
hour = time_aggregate.tm_hour
minute = time_aggregate.tm_min
second = time_aggregate.tm_sec


stddraw.setXscale(-1.5,1.5)
stddraw.setYscale(-1.5,1.5)

#draw circle
stddraw.setPenColor(stddraw.BLACK)
stddraw.setPenRadius(0.005)
stddraw.circle(0.0,0.0,1.2)
stddraw.setPenColor(stddraw.CYAN)
stddraw.circle(0.0,0.0,1.3)

#set up 1-12
stddraw.setFontSize(30)
stddraw.text(0,1,'12')
stddraw.text(1/2, math.sqrt(3)/2, '1')
stddraw.text(math.sqrt(3)/2, 1/2, '2')
stddraw.text(1, 0, '3')
stddraw.text(math.sqrt(3)/2, -1/2, '4')
stddraw.text(1/2, math.sqrt(3)/-2, '5')
stddraw.text(0,-1,'6')
stddraw.text(-1/2, math.sqrt(3)/-2, '7')
stddraw.text(math.sqrt(3)/-2, -1/2, '8')
stddraw.text(-1,0,'9')
stddraw.text(math.sqrt(3)/-2, 1/2, '10')
stddraw.text(-1/2, math.sqrt(3)/2, '11')

#second hand
stddraw.setPenRadius(0.001)
stddraw.setPenColor(stddraw.RED)
stddraw.line(0, 0, math.sin(math.radians(6*second)), math.cos(math.radians(6*second)))

#minute hand
stddraw.setPenRadius(0.01)
stddraw.setPenColor(stddraw.GRAY)
stddraw.line(0,0, math.sin(math.radians(6*minute)), math.cos(math.radians(6*minute)))

#hour hand
stddraw.setPenRadius(0.025)
stddraw.setPenColor(stddraw.BLACK)
stddraw.line(0, 0, math.sin(math.radians(30*hour)), math.cos(math.radians(30*hour)))


stddraw.show()
