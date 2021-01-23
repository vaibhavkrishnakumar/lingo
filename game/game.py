import sys,random

def read_dictionary(length):
  filename = "../dictionary/words_{}.txt".format(length)
  file = open(filename, "r")
  out = file.readlines()
  file.close()
  return out

def play(length):
  words = read_dictionary(length)
  secret = random.choice(words).strip()
  print("Your {} letter Lingo starts with {}... ".format(length, secret[0]))
  playing = True
  while playing:
    guess = raw_input("Enter a guess\n").strip()
    print("Your guess was {}".format(guess))
    if guess_is_correct(secret, guess):
      play_again = raw_input("You're right!\nPlay again? Enter Y/N\n")
      playing = "Y" == play_again.upper()
    else:
      greens = calculate_greens(secret, guess)
      yellows = calculate_yellows(secret, guess)
      if greens:
        print("Your guess was incorrect, but you did get some letters right!")
        one, two, three = parse_greens(greens, guess)
        print("Word is of the form {}{}{}{}".format(secret[0], one, two, three))

def guess_is_correct(secret, guess):
  return secret == guess

# Green refers to a correct letter in the correct index
def calculate_greens(secret, guess):
  greens = set()
  for i in range(1, len(secret)):
    if (secret[i] == guess[i]):
      greens.add(i)
  return greens

# Yellow refers to a correct letter in an incorrect index
def calculate_yellows(secret, guess):
  return set()

def parse_greens(greens, guess):
  one = guess[1] if 1 in greens else "_"
  two = guess[2] if 2 in greens else "_"
  three = guess[3] if 3 in greens else "_"
  return one, two, three

if __name__ == "__main__":
  input = raw_input("Welcome to Lingo - choose 4 or 5 letter words to guess!:\n")
  length = int(input)
  play(length)
