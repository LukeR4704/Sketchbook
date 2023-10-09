def setup():
    size(500, 500)
    background(0)
    
distance = 12.0
angle = 53
flag_height = 0

def draw():
    global distance
    global angle
    global flag_height
    
    noStroke()
    fill(255, 255, 255)
    triangle(450, 100, 450, 450, 100, 450)
    
    # fill(0, 0, 255)
    # triangle(80, 100, 420, 100, 90, 430)
