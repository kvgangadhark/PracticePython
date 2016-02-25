def reverse_words(str):
  #go for it
  lst = str.split(" ")
  print (lst)
  output = []
  for each in lst:
      out1 = [x for x in each]
      out = []
      for indx in range(0,len(out1)):
          out.append(out1[len(out1) - indx -1])
      output.append("".join(out))
  return " ".join(output)
