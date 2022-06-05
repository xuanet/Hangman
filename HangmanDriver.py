import random

def createWordList(filename):
    """Creates word list from file"""

    f = open(filename)
    wordList = []
    for word in f:
        wordList.append(word.strip())
    return wordList

def wordLengthRange():
    """Asks user for range of word length used in game"""

    limit = input("Set word length range? y/n")
    if limit == 'n':
        return [0, 0]

    lower = input("Lower bound of word length?\n")
    while not lower.isdigit() or int(lower) < 1:
        print("Lower bound must be an integer >= 1")
        lower = input("Lower bound of word length?\n")

    upper = input("Upper bound of word length?\n")
    while not upper.isdigit() or int(upper) < int(lower):
        print("Upper bound must be an integer >= to the lower bound")
        upper = input("Upper bound of word length?\n")

    lower = int(lower)
    upper = int(upper)

    print([lower, upper])
    f = input("Confirm bounds? y/n")

    if f == 'y':
        return [lower, upper]

    return wordLengthRange()

def createNewWordList(wordList, lower, upper):
    """Creates a new word list with all words having a length within the
    specified range"""

    newList = []

    if lower == 0 and upper == 0:
        return wordList

    for word in wordList:
        if lower <= len(word) <= upper:
            newList.append(word)

    print("There are " + str(len(newList)) + " candidate words in this range.")
    return newList

def scan(word, letter):
    indices = []
    for i in range(len(word)):
        if word[i] == letter:
            indices.append(i)

    return indices

def updateTemplate(template, indices, letter):
    newTemplate = [x for x in template]
    for index in indices:
        newTemplate[index] = letter

    return newTemplate

def runGame():
    """Runs the game"""

    alphabet = list("qwertyuiopasdfghjklzxcvbnm")

    wordList = createWordList("lowerwords.txt")
    range = wordLengthRange()
    newList = createNewWordList(wordList, range[0], range[1])
    secretWord = random.choice(newList)
    maxMisses = int(input("How many misses allowed? 0 for infinite"))
    if maxMisses == 0:
        maxMisses = 26
    solved = False

    guessedSet = set([])
    misses = 0
    template = ["_" for char in secretWord]

    while misses < maxMisses and solved == False:
        print("                                         "+ " ".join(template))
        print("Already guessed " + str(guessedSet))
        print("You have " + str(maxMisses - misses) + " guesses left\n")

        guess = input("Guess letter:")

        while guess not in alphabet or guess in guessedSet:
            print("Your guess must be a letter not already guessed")
            guess = input("Guess letter:")

        updatePos = scan(secretWord, guess)

        if len(updatePos) == 0:
            print("This letter not in word")
            misses += 1
            guessedSet.add(guess)
            continue

        template = updateTemplate(template, updatePos, guess)
        guessedSet.add(guess)

        if "_" not in template:
            solved = True

    if misses == maxMisses:
        print("Game over, the word was " + secretWord)
        return False

    print(secretWord)
    print("You guessed the word!")
    return True


if __name__ == "__main__":

    playAgain = True
    wins = 0
    losses = 0

    while playAgain == True:
        won = runGame()
        if won == True:
            wins += 1
        else:
            losses += 1
        f = input("Play again? y/n")
        if f == 'n':
            playAgain = False

    print("Your final score is " + str(wins) + " wins and " + str(losses) + " losses.")













