import random
def quotescript():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #last = 13
  last = len(quotes) - 1 #Note: If you want to add or remove quotes from your text file, you could change the last variable to update automatically
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  quotescript()
