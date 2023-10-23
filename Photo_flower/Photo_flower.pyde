def setup():
    global cx, cy
    size(500, 500)
    colorMode(RGB)
    cx = width / 2
    cy = height /2
    
cx = 0
cy = 0
    
def draw():    
    global cx, cy
    num = 4
    theta = TWO_PI / 4
    
    background(34, 139, 34)
    noStroke()
    strokeWeight(5)
    for j in range(5):
        r = j * 20

        for i in range(num):
            angle = theta * i
            # c = (i / float(num)) * 255
            # cr = c
            
            x = cx + sin(angle + 0.7) * r
            y = cy + cos(angle + 0.5) * r
            fill(101, 67, 33)
            circle(250, 250, 40)
            
            noStroke()
            fill(238, 210, 2)
            circle(x, y, 70) 
        
