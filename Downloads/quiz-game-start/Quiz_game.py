from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

q_list = QuizBrain(question_bank)

while q_list.still_has_ques():
    q_list.next_question()

print("You have completed your Quiz.")
print(f"Your total score is {q_list.score}/{len(question_bank)}")