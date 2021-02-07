import sys,random

def play(length):
  WORDS = read_dictionary(length)
  TOTAL_GUESSES = 5

  playing = True

  while playing:
    secret = random.choice(WORDS).strip()
    print("You have {} guesses; your {} letter Lingo starts with {}... ".format(TOTAL_GUESSES, length, secret[0]))
    guessing = True
    num_guesses = 0

    while guessing and num_guesses < TOTAL_GUESSES:
      guess = read_guess(length)
      num_guesses = num_guesses + 1
      print("Your guess was {}".format(guess))

      if guess_is_correct(secret, guess):
        print("You're right!")
        guessing = False
        num_guesses = 0
        playing = play_again()
      else:
        greens = calculate_greens(secret, guess)
        yellows = calculate_yellows(secret, guess)
        if greens:
          print("Incorrect, but you did get some letters right!\nThe word is of the form {}{}".format(secret[0], parse_greens(greens, guess, "_")))
          if yellows:
            yellows_str = ", ".join(yellows)
            print("And the word contains these letters: {}".format(yellows_str))

        elif yellows:
          yellows_str = ", ".join(yellows)
          print("Incorrect, but the word does contain these letters: {}".format(yellows_str))
        else:
          print("Incorrect, try again: {}{}".format(secret[0], parse_greens(set(), guess, "_")))
    if num_guesses == TOTAL_GUESSES:
      print("You're out of guesses! The word was {}".format(secret))
      num_guesses = 0
      guessing = False
      playing = play_again()

def read_dictionary(length):
  filename = "../dictionary/words_{}.txt".format(length)
  file = open(filename, "r")
  out = file.readlines()
  file.close()
  return out

def read_guess(length):
  guess = raw_input("Enter a guess\n").strip().lower()
  # TODO Add check to verify word exists in dictionary
  while (len(guess) != length):
    guess = raw_input("{} isn't a valid guess, please enter a {} letter word!\n".format(guess, length)).strip().lower()
  return guess

def guess_is_correct(secret, guess):
  return secret == guess

def play_again():
  play_again = raw_input("Play again? Enter Y/N\n")
  return "Y" == play_again.upper()

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

# TODO Rename since not just used to parse greens
def parse_greens(green, guess, default):
  one = guess[1] if 1 in green else default
  two = guess[2] if 2 in green else default
  three = guess[3] if 3 in green else default
  four = guess[4] if 4 in green else "" if len(guess) == 4 else default
  return "".join((one, two, three, four))

if __name__ == "__main__":
  length = raw_input("Welcome to Lingo - choose 4 or 5 letter words to guess!:\n")
  play(int(length))
