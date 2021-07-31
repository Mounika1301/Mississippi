from collections import Counter
def most_frequent():
  a = input("please enter a string") 
  frequency_per_char = Counter(a)
  print ("Per char frequency in '{}' is :\n {}".format(a, str(frequency_per_char)))
most_frequent()
