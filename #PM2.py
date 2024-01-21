#PM2.5 Indertifier
import turtle
P = turtle.Pen()
PM = turtle.numinput("PM2.5","Please enter 2.5")
if PM >= 90 : 
    turtle.bgcolor('red')
    P.write("udara sedang sangat buruk", font  = ('Impact', 20,'normal'))
if 71 <= PM < 90 :
      turtle.bgcolor('blue')
      P.write("udara sedikit membaik", font  = ('Impact', 20,'normal'))
if PM <= 70 :
    turtle.bgcolor('green')
    P.write("udara sudah membaik", font  = ('Impact', 20,'normal'))
turtle.done()
   