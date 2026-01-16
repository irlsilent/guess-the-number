# Number Guessing Game

A simple number guessing game implemented in Python 3 and C. The user defines a range of numbers, and the system randomly selects a number within that range. The goal is to guess the number using as few attempts as possible. The game demonstrates basic programming concepts, including loops, conditionals, user input handling, and random number generation, and showcases cross-language implementation.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following installed on your machine:

- **Python 3**: [Download here](https://www.python.org/downloads/)  
- **C Compiler** (GCC or equivalent):
  - Windows: Install [MinGW](https://www.msys2.org/) or use Visual Studio  
  - Linux: `sudo apt install build-essential`  
  - Mac: `xcode-select --install`

### Installing

1. Clone the repository:

```
git clone https://github.com/irlsilent/guess-the-number.git
cd guess-the-number
```
2. Navigate to the Python folder and run the game:
```
cd python
python number_guess.py
```
3. Navigate to the C folder, compile, and run the game:
```
cd ../c
gcc number_guess.c -o number_guess
./number_guess   # or number_guess.exe on Windows
```
## Running the Tests

This project currently does not include automated tests.  
Future improvements may include unit tests for:

- Python game logic
- C game logic
- Input validation

**Example test (manual):**
```
1. Enter Lower Bound: 1
2. Enter Upper Bound: 100
3. Guess a number: 17
4. “You guessed too low. Try again” 
5. "You have 6 guesses left."

---
```
## Deployment

This is a local console-based game.  
To deploy for other users:

- Copy the folder to another machine with Python or a C compiler installed
- Run the executable or script as shown above

---

## Built With

- Python 3 – Main language for scripting
- C – Demonstrates cross-language implementation
- GCC / Compiler – To run C code

---

## Contributing

Please open issues or submit pull requests if you find bugs or want to add features such as:

- Input validation enhancements
- Replay functionality
- Difficulty levels
- Score tracking

---

## Versioning

This project uses simple versioning. The current version is v1.0 – initial implementation.

---

## Authors

- Thomas Loonis – Initial work

See GitHub contributors for any additional participants.

---

## License

This project is licensed under the MIT License – see the `LICENSE.md` file for details.

---

## Acknowledgments

- Inspired by simple number guessing games to demonstrate basic programming logic
- Hat tip to anyone whose tutorials or code examples helped shape this project

