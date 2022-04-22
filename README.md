# Wordle crack

A small program I wrote for fun that attempts to guess the correct word for the wordle game.

I uses a dictionary of english words and has an interactive command line interface, which accepts different kinds of commands to support the guessing process.

## Commands
* example - returns one random word of the current set of words
* all - returns the first 20 words of the current set to limit the output
* has $x - will remove all words that do not contain $x, $x can be a single char or multiple chars like abc, which allows to submit multiple chars at once
* has not $x - same as "has" but the other way around.
* has at $x [1-5] - similar to has but takes only  one char and a position 1-5 parameter, so if you know in the first position is an a "has at a 1"
* has not at $x [1-5] - same as "has at" but the other way around.