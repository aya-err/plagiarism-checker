from difflib import SequenceMatcher

def check_similarity(path1, path2):
    with open(path1) as file_one, open(path2) as file_two:
        data1 = file_one.read()
        data2 = file_two.read()
    matches = SequenceMatcher(None, data1, data2).ratio()
    return matches*100

result = check_similarity("file1.txt", "file2.txt")
print(f"The plagiarized content is {result:.1f}%")