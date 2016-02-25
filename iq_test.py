def iq_test(numbers):
    #your code here
    even_count = 0
    odd_count = 0
    even_position = 0
    odd_postion = 0
    
    for each in numbers:
      if each %2 ==0:
        even_count += 1
        even_position = numbers.index(each)
      else:
        odd_count += 1
        odd_position = numbers.index(each)
    if even_count == 1:
      return even_position
    else:
      return odd_postion


iq_test(
