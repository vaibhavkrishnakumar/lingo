import sys,random

def read_dictionary(length):
  filename = "../dictionary/words_{}.txt".format(length)
  file = open(filename, "r")
  out = file.readlines()
  file.close()
  return out

def play(length):
  words = read_dictionary(length)
  playing = True
  while (playing):
    secret = random.choice(words)
    guess = raw_input("Your {} letter Lingo starts with {}... Enter a guess\n".format(length, secret[0]))
    print("Your guess was {}".format(guess))
    if (secret == guess): # TODO Fix equality check
      print("You're right!")
    else:
      print("Incorrect")
    playing = False


if __name__ == "__main__":
  input = raw_input("Welcome to Lingo - choose 4 or 5 letter words to guess!:\n")
  length = int(input)
  play(length)
