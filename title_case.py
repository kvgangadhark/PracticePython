def title_case1(word):
    output = []
    lst = [x for x in word]
    print(lst)
    print (lst[1])
    for index in range(0,len(lst)):
        if index == 0:
            print (lst[index])
            output.append(lst[index].upper())
        else:
            output.append(lst[index])
    print (''.join(output))

def title_case(title, minor_words):
  output = []
  m1 = minor_words.split(' ')
  m2 = [x.lower() for x in m1]
  if (title == ''):
    return ''
  lst = title.split(' ')
  is_first_word = True
  for each in lst:
    if each.lower() in m2 and is_first_word != True:
      output.append(each.lower())
    else:
      is_first_word = False
      out1 = []
      lst1 = [x for x in each]
      for index in range(0,len(lst1)):
        if index == 0:
          out1.append(lst1[0].upper())
        else:
          out1.append(lst1[index].lower())
      output.append("".join(out1))
  return  " ".join(output)

print (title_case("a clash of kings",'a of an the'))
