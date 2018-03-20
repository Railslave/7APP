def pyCopy(source, target, destX, destY):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      setColor(getPixel(target, x + destX, y + destY), color)
  return(target)

  
def chromakey(source, target, destX, destY):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      if distance(color, red) > 50:
        setColor(getPixel(target, x + destX, y + destY), color)
  return(target)
        
        
 
def card():
  final = makeEmptyPicture(2100, 1500)
  
  #Background
  background = makePicture(pickAFile())
  pyCopy(background, final, 0, 0)
  
  #Picture 1
  pic1 = makePicture(pickAFile())
  chromakey(pic1, final, 650, 150)
  

  
  
  #Picture 2
  pic2 = makePicture(pickAFile())
  chromakey(pic2, final, 75, 1315)
  
  
  #Picture 3
  pic3 = makePicture(pickAFile())
  chromakey(pic3, final, 954, 1290)
  
  
  #Picture 4
  pic4 = makePicture(pickAFile())
  chromakey(pic4, final, 1600, 900)
  show (final)
  writePictureTo(final, "C://Users//Ryan//Desktop//final.jpg")
  
  
  