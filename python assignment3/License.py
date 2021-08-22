'''
2. Driver’s License Exam
The local driver’s license office has asked you to
create an application that grades the written portion of the driver’s license exam.
The exam has 20 multiple-choice questions. Here are the correct answers:
1. B 6. A 11. B 16. C
2. D 7. B 12. C 17. C
3. A 8. A 13. D 18. B
4. A 9. C 14. A 19. D
5. C 10. D 15. D 20. A
Your program should store these correct answers in a list.
The program should read the student’s answers for
each of the 20 questions from a text file and store the answers in another list.
(Create your own text file to test the application.)
After the student’s answers have been read from the file,
the program should display a message indicating
whether the student passed or failed the exam.
(A student must correctly answer 15 of the 20 questions to pass the exam.)
It should then
display the total number of correctly answered questions,
the total number of incorrectly answered questions, and
a list showing the question numbers of the incorrectly answered questions.
'''

NUM_QUESTIONS = 20  # number of questions on the test
def main():
    correct_answers = read_answers('answers.txt')
    student_answers = read_answers('student_answers.txt')
    incorrect = 0  # number of incorrect answers
    incorrect_answers = list() # list holds the numbers student got wrong

    # compare student's answers to correct answers
    for index in range(len(correct_answers)):
        if correct_answers[index] != student_answers[index]:
            incorrect += 1
            # if answer is wrong, append to list
            incorrect_answers.append(index + 1)
    correct = NUM_QUESTIONS - incorrect
    if correct >= 15:
        print('You Passed')
    else:
        print('You Failed')
    print('Number of correct answers:', correct)
    print('Number of incorrect answers:', incorrect)
    print('The questions you got wrong were:', incorrect_answers)

# function reads in both the answer file and student's answers in order to reuse code
def read_answers(file):
    answers_list = list()
    answers_file = open(file, 'r')
    for ans in range(NUM_QUESTIONS):
        answers_list.append(answers_file.readline().strip("1234567890. \n").upper())
        # .strip() - removes numbers, periods, whitespaces, and newlines
        # .upper() - because of case sensitivity
    answers_file.close()
    return answers_list

main()




# answers_list[ans] = answers_file.readline().strip("1234567890. \n").upper()
# answers_list = [0] * NUM_QUESTIONS # an empty list that can hold 20 items
# if a number, period, or white space is present, strip will remove it