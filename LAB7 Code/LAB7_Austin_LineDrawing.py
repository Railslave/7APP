def betterBAndW(source):
  pixels = getPixels(source)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    newColor = makeColor((r * 0.299) + (g * 0.587) + (b * 0.114) / 3)
    setColor(p, newColor)
  writePictureTo(source, "F://CSUMB//CST205//JES//LAB7//Results//line_drawing_bandw.jpg")
  show(source)

def lineDraw(source, contrast):
  #target = makeEmptyPicture(getWidth(source), getHeight(source))
  newPic = betterBAndW(source)
  show(newPic)
  for x in range(0, getWidth(source) - 1):
    for y in range(0, getHeight(source) - 1):
      zero = getPixel(newPic, x, y)
      down = getPixel(newPic, x, y + 1)
      right = getPixel(newPic, x + 1, y)
      avgZero = (getRed(zero) + getGreen(zero) + getBlue(zero)) / 3
      avgDown = (getRed(down) + getGreen(down) + getBlue(down)) / 3
      avgRight = (getRed(right) + getGreen(right) + getBlue(right)) / 3
      if abs(avgZero - avgDown) > contrast and abs(avgZero - avgRight) > contrast:
        setColor(zero, black)
      if abs(avgZero - avgDown) <= contrast and abs(avgZero - avgRight) <= contrast:
        setColor(zero, white)
  repaint(newPic)
  writePictureTo(newPic, "F://CSUMB//CST205//JES//LAB7//Results//line_drawing.jpg")
  show(newPic)