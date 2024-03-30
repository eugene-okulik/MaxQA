import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path to the file to analyze")
parser.add_argument("search", help="Path to the file to analyze")

args = parser.parse_args()

path = args.path
search = args.search

for file in os.listdir(path):
    cur_path = os.path.join(path, file)
    if os.path.isfile(cur_path):
        with open(cur_path, 'r') as file:
            lines = file.readlines()
            for number, line in enumerate(lines, 1):
                if search in line:
                    words = list(line.split())
                    search_index = words.index(search)
                    if search_index <= 4:
                        print(' '.join(words[0:search_index + 6]))
                    else:
                        print(' '.join(words[search_index - 5:search_index + 6]))
