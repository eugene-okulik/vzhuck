import argparse
import sys
import os


def print_python_version():
    print(sys.version)


def extract_context(line, word):
    words = line.split()
    try:
        index = words.index(word)
    except ValueError:
        return None
    start = max(index - 5, 0)
    end = min(index + 6, len(words))
    context = ' '.join(words[start:end])
    return context


def read_file(filename, text):
    with open(filename, encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            if text in line:
                context = extract_context(line, text)
                if context:
                    print(
                        f"Text found in file '{filename}', "
                        f"in line #{line_num}: {context}"
                    )


parser = argparse.ArgumentParser()
parser.add_argument("path", help="Folder path")
parser.add_argument("-t", "--text", help="text for search")
args = parser.parse_args()
print(args.path, args.text)
if not os.path.isdir(args.path):
    print("Folder does not exist")
    exit(-1)
filenames = os.listdir(args.path)
for f in filenames:
    f_path = os.path.join(args.path, f)
    read_file(f_path, args.text)
