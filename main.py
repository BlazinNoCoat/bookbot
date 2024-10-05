def main():
    path_to_file="books/frankenstein.txt"   
    print(f"--- Begin report of {path_to_file} ---")
    with open(path_to_file) as f:
        file_contents = f.read()
        words=file_contents.split()
        lowered_string=file_contents.lower()
        character_count={}
        for char in lowered_string:
            if char in character_count:
                character_count[char] +=1
            else:
                character_count[char]=1
    print(f"{len(words)} words found in the document")
    for char in character_count:
        print(f"The '{char}' character was found {character_count[char]} times")





main()