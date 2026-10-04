# plagirism-checker
This project checks the plagiarism percentage between two given files using Pyhton.

## How it works
The program reads two text files and uses Python's built-in `difflib.SequenceMatcher` to measure how much of their content matches. The result is printed as a similarity percentage.

## Requirements
- Python 3.x 

## Usage
1. Put the two texts you want to compare in `file1.txt` and `file2.txt`.
2. Run the program:

```
python checker.py
```

## Example output
```
The plagiarized content is 71.3%
```

## Project structure
```
plagiarism-checker/
├── checker.py    # main program
├── file1.txt     # first text to compare
├── file2.txt     # second text to compare
└── README.md
```

## Author

Aya
