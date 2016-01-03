# 12 Distance between two points on Earth
from math import acos,sin,cos, radians

def calcDistanceOnEarth():
	print ("Please give t1, t2, g1, g2 seperated by whitespace ")
	t1,t2,g1,g2=map(int,input().split())
	print (6371.01 * radians(acos((sin(t1)*sin(t2)) + (cos(t1)*cos(t2)*cos(g1-g2)))))
	print ("sth")

calcDistanceOnEarth()