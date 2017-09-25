u = 0
t = int(input("Time spend on the road: "))
a = int(input("Acceleration: "))
s = int(input("Distance: "))
speed_limit = 60

v = int(u + a*t)
d = (a*(t**2)/2)
for i in range (t+1):
    print("Duration",i,"Distance","*"*int((a*(i**2)/2)/10))

if v > 60:
    print("The person went over the speed limit","reached",v,"m/s")
else:
    print("The person did not reach the speed limit","Max speed was",v,"m/s")

if d >= s:
    print("Reach destination",d,"m")
else:
    print("Did not reach destination")
