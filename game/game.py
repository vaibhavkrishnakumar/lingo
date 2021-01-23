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
  while playing:
    secret = random.choice(words).strip()
    print("Your {} letter Lingo starts with {}... ".format(length, secret[0]))
    guessing = True
    while guessing:
      guess = read_guess(length)
      print("Your guess was {}".format(guess))
      if guess_is_correct(secret, guess):
        play_again = raw_input("You're right!\nPlay again? Enter Y/N\n")
        guessing = False
        playing = "Y" == play_again.upper()
      else:
        greens = calculate_greens(secret, guess)
        yellows = calculate_yellows(secret, guess)
        if greens:
          one, two, three = parse_greens(greens, guess, "_")
          # TODO only works for 4 letter words, fix
          print("Incorrect, but you did get some letters right!\nThe word is of the form {}{}{}{}".format(secret[0], one, two, three))
          if yellows:
            yellows_str = ", ".join(yellows)
            print("And the word contains these letters: {}".format(yellows_str))
        elif yellows:
          yellows_str = ", ".join(yellows)
          print("Incorrect, but the word does contain these letters: {}".format(yellows_str))
        else:
          # TODO only works for 4 letter words, fix
          print("Incorrect, try again: {}___".format(secret[0]))

def read_guess(length):
  guess = raw_input("Enter a guess\n").strip().lower()
  while (len(guess) != length):
    guess = raw_input("{} isn't a valid guess, please enter a {} letter word!\n".format(guess, length)).strip().lower()
  return guess

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
  yellows = set()
  for i in range(1, len(secret)):
    if guess[i] in secret and guess[i] != secret[i]:
      yellows.add(guess[i])
  return yellows

# TODO only works for 4 letter words, fix
def parse_greens(green, guess, default):
  one = guess[1] if 1 in green else default
  two = guess[2] if 2 in green else default
  three = guess[3] if 3 in green else default
  return one, two, three

if __name__ == "__main__":
  input = raw_input("Welcome to Lingo - choose 4 or 5 letter words to guess!:\n")
  length = int(input)
  play(length)
