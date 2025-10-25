from Question import Question

question_prompts = [
    "What color are Apple? \n(a) Red \n (b) Purple \n (c) Orange\n\n",
    "What color are Bananas? \n(a) Yellow \n (b) Magenta \n (c) Orange\n\n",
    "What color are Strawberries? \n(a) Red \n (b) Purple \n (c) Orange\n\n"

]

question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(question):
    score = 0
    for question in question:
        answer = input(question.prompts)
        if answer == question.answer:
            score +=1

    print("you got " + str(score) + "/" + str(len(question)) + "correct")
    run_test (question)