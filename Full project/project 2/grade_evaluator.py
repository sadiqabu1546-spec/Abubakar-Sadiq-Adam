score_input = input("Enter the student's numerical score (0-100): ")
score = int(score_input)

if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    if score >= 90:
        print("The grade is: A")
        # Nested logic for the 'A' challenge
        if score == 100:
            print("Perfect Score! Excellent work!")
        elif score <= 94:
            print("Great start to an A! Keep it up!")
        else:
            print("Solid A! Well done!")
    elif score >= 79:
        print("The grade is: B")
    elif score >= 69:
        print("The grade is: C")
    elif score >= 60:
        print("The grade is: D")
    else:
        print("The grade is: F")