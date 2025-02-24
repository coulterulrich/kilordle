from words import WORDLES, WORDS
import time

def seedRandom(numWordles):
    pstNow = time.time() - 2880000
    return pstNow // 86400000

def genWorldList(wordles, length = 1000):
    
    numWordles = len(wordles)
    
    wordList = []
    generator = 163
    random = seedRandom(numWordles)
    
    for i in range(length):
        wordList.append(wordles[int((random + generator * i) % numWordles)])
        
    return wordList
    
class wordle:
    def __init__(self, word):
        self.word = word
        self.correct = [False] * len(word)
        self.clues = []
        self.solved = False
        self.score = 0
            
    def __str__(self):
        if len(self.clues) <= 0:
            return ''.join(self.correct)
        else:
            return clues[len(self.clues) - 1]
            
    def guess(self, word):
        # setup clue buffer
        clue = [0] * len(self.word)
        
        # loop the guess, fill out correct array
        # fill out correct clue first so extra misplaced letters don't take priority
        for i in range(len(word)):
            letter = word[i]
            if i >= len(self.word) or letter != self.word[i]:
                continue
            clue[i] = 2
            self.correct[i] = True
                        
        # loop the guess, fill out misplaced letters
        for i in range(len(word)):
            letter = word[i]
            if i >= len(self.word) or letter == self.word[i]:
                continue
                
            # in the case of multiple letters
            # mark misplaced if the current clue count is below the letter frequency
            letterCount = 0
            for j in range(len(self.word)):
                if self.word[j] == letter:
                    letterCount += 1
            for j in range(len(clue)):
                if clue[j] == 2 and word[j] == letter:
                    letterCount -= 1
            if (letterCount > 0):
                clue[i] = 1
        
        # save clue to the clue history
        self.clues.append(clue)
        
        # solved if correct is all true
        self.solved = all(self.correct)
        
        # calculate score sort value
        self.score = 0
        for i in range(min(5, len(self.clues))):
            clue = self.clues[len(self.clues) - i - 1]
            for j in range(len(clue)):
                self.score += clue[j]
        
    
class kilowordle:
    def __init__(self, wordles, words, length = 1000):
        self.wordSet = set(words)
        self.wordSet.update(wordles)
        self.wordles = []
        self.guesses = []
        self.solved = 0
        wordList = genWorldList(wordles)
        for word in wordList:
            self.wordles.append(wordle(word))
            
    def guess(self, word):
        word = word.lower()
        if len(word) != 5 or not word in self.wordSet:
            return False
            
        self.guesses.append(word)
        for wordle in self.wordles:
            if wordle.solved:
                continue
                
            wordle.guess(word)
            if wordle.solved:
                self.solved += 1
        return True
                
    def print(self, length = 12, columns = 4):
        topBoards = sorted(
            [w for w in self.wordles if not w.solved],  # only boards not solved
            key=lambda w: -w.score  # sort by sort value
        )
        
        remaining = len(topBoards)
        length = min(length, remaining)
        del topBoards[length:]
        
        if remaining > length:
            print()
            print(f"+ {remaining - length} more...")
            print()
        
        for i in range(0, length, columns):
            # print header
            for k in range(columns):
                wordleIndex = length - (i + k) - 1
                if wordleIndex < 0:
                    break
                if k != 0:
                    print('     ', end='')
                print('_____________', end='')
            print()
            
            for j in range(6):
                offset = max(0, 5 - len(self.guesses))
                guessIndex = len(self.guesses) - 5 + j + offset
                guess = self.guesses[guessIndex] if guessIndex >= 0 and guessIndex < len(self.guesses) else None
                
                # print guess
                for k in range(columns):
                    wordleIndex = length - (i + k) - 1
                    if wordleIndex < 0:
                        break
                    if k != 0:
                        print('     ', end='')
                    print('[ ', end='')
                    if guess is None:
                        print('          ', end='')
                    else:
                        for letter in guess:
                            print(letter, end='')
                            print(' ', end='')
                    print(']', end='')
                                
                print()
                                    
                # print clue
                if guess is None:
                    print(end='')
                else:
                    for k in range(columns):
                        wordleIndex = length - (i + k) - 1
                        if wordleIndex < 0:
                            break
                        if k != 0:
                            print('     ', end='')
                        wordle = topBoards[wordleIndex]
                        clue = wordle.clues[guessIndex]
                        print('  ', end='')
                        for code in clue:
                            if code == 1:
                                print('~ ', end='')
                            elif code == 2:
                                print('# ', end='')
                            else:
                                print('  ', end='')
                        print(' ', end='')
                                                
                print()
            print()

length = 1000
game = kilowordle(WORDLES, WORDS, length)
quit = False
while not quit:
    guess = input("Input a 5 letter word: ").lower()
    if (guess == "q" or guess == "quit"):
        quit = True
        break
        
    if not game.guess(guess):
        print(f"{guess} is not a valid word!")
    elif game.solved == length:
        quit = True
        print(f"You won in {len(game.guesses)} guesses!")
        break
    else:
        game.print()
        print(f"Solved {game.solved} / {length} | {length - game.solved} remaining...")
        print()
