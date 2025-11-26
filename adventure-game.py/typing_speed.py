import sys, time, random
typing_speed = 150
def slow_type(t):
    for i in t:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(random.random()*10/typing_speed)
 

 