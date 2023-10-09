def setup():
    global cx
    global cy
    global r
    global theta
    global c
    # fullScreen()
    size(1000, 1000)
    cx = width / 2
    cy = height / 2
    background(0)
    
    colorMode(HSB)
    
cx = 0
cy = 0
r = 10
theta = 0
c = 0

def draw():
    global cx
    global cy
    global r
    global theta
    global c
    x = cx + sin(theta) * r
    y = cy + cos(theta) * r
    
    fill(c, 255, 255)
    # strokeWeight(20)
    circle(x, y, 10)
    
    r = r + 1.5
    c = (c + 1) % 256
    theta = theta + 90
