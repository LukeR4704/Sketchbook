def setup():
    global cx
    global cy
    global r
    size(500, 500)
    colorMode(HSB)
    cx = width / 2
    cy = height / 2
    
cx = 0
cy = 0
r = 100
angle2 = 0
    # a = 1
    # b = 1
    # print(a)
    # print(b)
    
    # for i in range(100):
    #     ab = a + b
    #     a = b
    #     b = ab
    #     print(ab)
    
def draw():
    global cx
    global cy
    global r
    global angle2
    num = 12
    theta = TWO_PI / 12
    
    background(0)
    noStroke()
    strokeWeight(5)
    for j in range(10):
        r = j * 20
        a = j * 30
        for i in range(num):
            angle = theta * i
            c = (i / float(num)) * 255
            c = (c + mouseX) % 256
            cr = i * j
            fill(c, 255, a)
            
            x = cx + sin(angle + mouseY) * r
            a3 = map(cos(angle2), -1, 1, 50, 200)
            y = cy + cos(angle) * r
            stroke(200, 255, 255, a)
            line(cx, cy, x, y)
            noStroke()
            circle(x, y, a3)
            angle2 += 0.0001
