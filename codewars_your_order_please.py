def order(sentence):
  # code here
  dict1 = {}
  output = []  
  list = sentence.split(" ")
  for each in list:
    clist = [x for x in each]
    for index in range(1,10):
      if str(index) in clist:
        dict1[index] = "".join(clist)
  for index in range(1,10):
    if  dict1.has_key(index)
      output.append(dict1[index])
  return " ".join(output)


order("is2 Thi1s T4est 3a")
