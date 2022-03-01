from question_model import Question
from data import get_questions
from quiz_brain import QuizBrain
from ui import Interface

def quiz_game():
    question_bank = []
    question_data = get_questions()

    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = Interface(quiz)

    if quiz_ui.continue_quiz:
        quiz_game()

quiz_game()



# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("You've completed the quiz")

