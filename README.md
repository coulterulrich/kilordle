# Command Usage
1. Run `kilowordle.py`
2. Guess 5 letter words to solve the wordles

# Clues
1. `#` is correct
2. `~` is misplaced
```
_____________     _____________     _____________     _____________
[ t r u c k ]     [ t r u c k ]     [ t r u c k ]     [ t r u c k ]
  ~ ~   #             #   ~ #         # # #   #           ~        
[ r e l a x ]     [ r e l a x ]     [ r e l a x ]     [ r e l a x ]
  # #   ~           ~ ~   #           ~                 # # # #    
[           ]     [           ]     [           ]     [           ]

[           ]     [           ]     [           ]     [           ]

[           ]     [           ]     [           ]     [           ]

[           ]     [           ]     [           ]     [           ]
```

# Programmatic Docs

## `kilowordle(wordleWordList, boardLength = 1000)`
- `.wordles`: List of all `wordle` board objects
- `.guesses`: List of previous guesses
- `.solved`: Count of solved boards
- `.guess(word)`: Guesses a word
- `.print()`: Prints the top boards


## `wordle(word)`
- `.word`: The secret word of this board
- `.correct`: List of 5 booleans for correctly guessed places
- `.clues`: List of previous clues, each clue is a list of 5 integers from the given guess word
  - 0 = Bad
  - 1 = Misplaced
  - 2 = Correct
- `.solved`: If this board is solved
- `.score`: The sorting score of this board, higher means it's closer to being solved

