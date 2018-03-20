def snowman(pic):
  w, h = getWidth(pic), getHeight(pic)
  canvas = makeEmptyPicture(w, h)
  for x in range(0, w):
    for y in range(0, h):
      c = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x, y), c)
  addOvalFilled(canvas, 860, 805, 300, 250, white)
  addOvalFilled(canvas, 885, 650, 250, 200, white)
  addOvalFilled(canvas, 910, 500, 200, 175, white)
  addOvalFilled(canvas, 967, 618, 10, 10, black)
  addOvalFilled(canvas, 986, 625, 10, 10, black)
  addOvalFilled(canvas, 1010, 628, 10, 10, black)
  addOvalFilled(canvas, 1035, 625, 10, 10, black)
  addOvalFilled(canvas, 1053, 618, 10, 10, black)
  addOvalFilled(canvas, 1013, 591, 12, 12, red)
  addOvalFilled(canvas, 957, 557, 15, 15, black)
  addOvalFilled(canvas, 1039, 557, 15, 15, black)
  show(canvas)
  writePictureTo(canvas, "F://CSUMB//CST205//JES//LAB7//Results//snowman_desert.jpg")
  