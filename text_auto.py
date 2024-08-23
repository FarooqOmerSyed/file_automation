# Read input.txt and remove unwanted words
with open("randomtxt.txt") as fin:
    lines = fin.readlines()
    unwanted_words = ["--[gibberish]--"]  # Add your unwanted words here
    cleaned_lines = [line.replace(word, "") for line in lines for word in unwanted_words]

# Write cleaned lines to output.txt
with open("output.txt", "w") as fout:
    fout.writelines(cleaned_lines)
