def run_diary_exercise():
    with open("diary.txt","w") as f:
        f.write("Day 1: Started python learning. \n")
        f.write("Day 2: Mastered list sequences. \n")
        f.write("Day 3: Exploring safe file I/O. \n")

        try:
            with open("diary.txt","r") as f:
                print(f.read())
        except FileNotFoundError:
                print("Diary file is currently missing")
        try:
             with open("missing.txt", "r") as f:
                  content = f.read()
                  print(content)
        except FileNotFoundError:
             print("Safe exit: missing.txt not found")

run_diary_exercise()