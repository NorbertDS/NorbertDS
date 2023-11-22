import turtle
import random

# Part (i): Program Design

# Name: Your Name
# University ID: Your University ID
# Section Number: Your Section Number

"""
Program Design:

Purpose:
   Simulate auto grading of an online quiz with multiple choice questions. 
   Generate model and student answers randomly, calculate the score, and visualize the answers using Turtle Library.

Input:
   None (answers are generated randomly)

Output:
   Display the result with encoded answers and visualize the answers using a bar chart.

Algorithm:
   1. Define answerGenerator() to generate random model and student answers.
   2. Define encodeAnswer() to encode the answers as specified.
   3. Define computeScore() to calculate the score of correct and incorrect answers.
   4. Define drawBar() to draw one bar in the Turtle chart.
   5. Define drawResult() to visualize the encoded model and student answers using Turtle.

Test Plan:
   1. Generate model and student answers.
   2. Encode the answers.
   3. Calculate and display the score.
   4. Visualize the answers using Turtle Library.
"""

# Part (ii): Python Program

# Function to generate random answers
def answerGenerator(num_questions):
    import random
    choices = ['A', 'B', 'C', 'D']
    return ''.join(random.choices(choices, k=num_questions))

# Function to encode the answer
def encodeAnswer(answer):
    encoded = ""
    count = 1
    for i in range(1, len(answer)):
        if answer[i] == answer[i - 1]:
            count += 1
        else:
            encoded += str(count) + answer[i - 1]
            count = 1
    encoded += str(count) + answer[-1]
    return encoded

# Function to compute the score
def computeScore(model_answers, student_answers):
    score = 0
    for model, student in zip(model_answers, student_answers):
        if model == student:
            score += 1
    return score

# Function to draw one bar in the chart
def drawBar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height * 50)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(height * 50)
    t.left(90)
    t.end_fill()
    t.forward(5)


# Function to visualize encoded answers using Turtle
def drawResult(encoded_model, encoded_student):
    window = turtle.Screen()
    window.title("Bar Chart of Answers")
    window.bgcolor("lightgray")

    chart_turtle = turtle.Turtle()
    chart_turtle.color("black")
    chart_turtle.fillcolor("blue")
    chart_turtle.speed(10)

    # Draw bars for encoded model answers
    chart_turtle.penup()
    chart_turtle.goto(-100, 250)
    chart_turtle.write("Model Answer",align="left", font=("Arial", 10, "normal"))

    chart_turtle.penup()
    chart_turtle.goto(-300, 100)
    for encoded_answer in encoded_model:
        if encoded_answer.isdigit():
            drawBar(chart_turtle, int(encoded_answer))

        chart_turtle.write(encoded_answer, align="center")
        chart_turtle.forward(5)


    # Draw bars for encoded student answers
    chart_turtle.penup()
    chart_turtle.goto(-100, 80)
    chart_turtle.write("Student Answer",align="left", font=("Arial", 10, "normal"))

    chart_turtle.penup()
    chart_turtle.goto(-300, -100)
    chart_turtle.fillcolor("red")
    for encoded_answer in encoded_student:
        if encoded_answer.isdigit():
            drawBar(chart_turtle, int(encoded_answer))
        
        chart_turtle.write(encoded_answer, align="center")
        chart_turtle.forward(5)

    chart_turtle.hideturtle()
    window.mainloop()

# Generating model and student answers
num_questions = 10
model_answers = answerGenerator(num_questions)
student_answers = answerGenerator(num_questions)

# Computing and displaying the score
score = computeScore(model_answers, student_answers)
encoded_model = encodeAnswer(model_answers)
encoded_student = encodeAnswer(student_answers)

def displayResult():
    print(
"""======================================================================================
                    This is a simulation of online auto grading 
                    Model and student answers are generated randomly
======================================================================================
Model Answer: {}
Student Answer: {}
Encoded Model Answer: {}
Encoded Student Answer: {}
======================================================================
                        Results Table
======================================================================
Question Number\t\t Your Answer\t\tCorrect Answer
======================================================================"""
.format(model_answers, student_answers, encoded_model, encoded_student))
    for i in range(1, 11):
        if student_answers[i - 1] != model_answers[i - 1]:
            print(
            """\t{}\t\t\t{}*\t\t\t{}
------------------------------------------------------------------------"""
        .format(i, student_answers[i - 1], model_answers[i - 1]))
        else:
            print(
                """\t{}\t\t\t{}\t\t\t{}
------------------------------------------------------------------------"""
.format(i, student_answers[i - 1], model_answers[i - 1]))
    print("========================================================================")
    print("* means incorrect answer")
    print(f"Score: {score}/{num_questions}")
    print(f"Incorrect Answers: {num_questions - score}")


#   Displaying the results
displayResult()

#   Drawing the results bar chart using Turtle
drawResult(encoded_model, encoded_student)


