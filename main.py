from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

brain = QuizBrain(question_bank)
brain.next_question()

while brain.still_has_questions():
    brain.next_question()

print("You have completed the quiz")
print(f"Your score is {brain.score}/{brain.question_number}")
