def high_score():
    student_score = [78,65,89,86,55,91,64,89]
    high_score = student_score[0]
    for i in student_score:
        if i > high_score:
            high_score = i
    print(high_score)
def main():
    high_score()

if __name__ == "__main__":
    main()