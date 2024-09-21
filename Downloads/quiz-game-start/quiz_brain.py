class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    def still_has_ques(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        #print(self.question_list)
        user_answer = input(f"{self.question_number}: {current_question.text}(true/false):")
        self.correct_answer(user_answer, current_question.answer)

    def correct_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Your answer is correct!")
            print(f"Your current score is {self.score}/{self.question_number}")

        else:
            print("Your answer is wrong!")

