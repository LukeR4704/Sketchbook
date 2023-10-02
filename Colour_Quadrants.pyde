def setup():
  size(500, 500)
  
def draw():
  background(255, 255, 255)
  noStroke()
  fill(210, 125, 45)
  if mouseX <= 250 and mouseY <= 250:
    rect(0, 0, 250, 250)
  elif mouseX <= 250 and mouseY > 250:
    fill(191, 64, 191)
    rect(0, 250, 250, 250)
  elif mouseX > 250 and mouseY <= 250:
    fill(0, 150, 255)
    rect(250, 0, 250, 250)
  else:
    fill(80, 200, 120)
    rect(250, 250, 250, 250)
