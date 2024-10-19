import random
import tkinter as tk

# Define a set of questions for trigonometry and algebra
trigonometry_questions = [
    {"question": "What is sin(0 degrees)?", "answer": "0.0"},
    {"question": "What is sin(30 degrees)?", "answer": "0.5"},
    {"question": "What is sin(90 degrees)?", "answer": "1.0"},
    {"question": "What is sin(180 degrees)?", "answer": "0.0"},
    {"question": "What is cos(0 degrees)?", "answer": "1.0"},
    {"question": "What is cos(60 degrees)?", "answer": "0.5"},
    {"question": "What is cos(90 degrees)?", "answer": "0.0"},
    {"question": "What is cos(180 degrees)?", "answer": "-1.0"},
]
algebra_questions = [
    {"question": "Expand: a^2 - b^2", "answer": "(a-b)(a+b)"},
    {"question": "Expand: (a + b)^2", "answer": "a^2+2ab+b^2"},
    {"question": "Expand: a^2 + b^2", "answer": "(a+b)^2-2ab"},
    {"question": "Expand: (a - b)^2", "answer": "a^2-2ab+b^2"},
    {"question": "Expand: (a + b + c)^2", "answer": "a^2+b^2+c^2+2ab+2bc+2ca"},
    {"question": "Expand: (a - b - c)^2", "answer": "a^2+b^2+c^2-2ab+2bc-2ca"},
    {"question": "Expand: (a + b)^3", "answer": "a^3+3a^2b+3ab^2+b^3"},
    {"question": "Expand: (a + b)^3", "answer": "a^3+b^3+3ab(a+b)"},
]



def ask_question(question):
    user_answer = input(question["question"] + " ")
    return user_answer == question["answer"]


def run_study_session():
    print("Welcome to the Math Revision Flashcards!")
    topic = input("Choose a topic: Trigonometry or Algebra? ").strip().lower()

    if topic == "trigonometry":
        questions = trigonometry_questions
    elif topic == "algebra":
        questions = algebra_questions
    else:
        print("Invalid topic. Please restart the session and choose a valid topic.")
        return

    correct_answers = 0
    total_questions = len(questions)

    for question in random.sample(questions, total_questions):
        if ask_question(question):
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect.")

    print(f"Study session complete. You answered {correct_answers} out of {total_questions} questions correctly.")


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Revision Flashcards")

        self.frame = tk.Frame(root, padx=10, pady=10, bd=2, relief="groove")
        self.frame.pack(pady=20)

        self.question_label = tk.Label(self.frame, text="Choose a topic to start", font=('Helvetica', 14),
                                       wraplength=400)
        self.question_label.pack(pady=20)

        self.entry = tk.Entry(root, font=('Helvetica', 14))
        self.entry.pack(pady=10)

        self.note_label = tk.Label(root, text="Note: Please enter answers in float format", font=('Helvetica', 10),
                                   fg="blue")
        self.note_label.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=('Helvetica', 14),
                                       bg="lightblue")
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=('Helvetica', 14))
        self.result_label.pack(pady=20)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, font=('Helvetica', 14),
                                     bg="lightgreen")
        self.next_button.pack(pady=10)

        self.topic = None
        self.questions = []
        self.current_question = None
        self.correct_answers = 0
        self.total_questions = 0

        self.topic_menu()

    def topic_menu(self):
        self.topic_label = tk.Label(self.root, text="Choose a topic:", font=('Helvetica', 14))
        self.topic_label.pack(pady=20)

        self.trig_button = tk.Button(self.root, text="Trigonometry", command=lambda: self.start_quiz('trigonometry'),
                                     font=('Helvetica', 14), bg="lightcoral")
        self.trig_button.pack(pady=10)

        self.algebra_button = tk.Button(self.root, text="Algebra", command=lambda: self.start_quiz('algebra'),
                                        font=('Helvetica', 14), bg="lightcoral")
        self.algebra_button.pack(pady=10)

    def start_quiz(self, topic):
        self.topic = topic
        self.questions = trigonometry_questions if topic == 'trigonometry' else algebra_questions
        self.total_questions = len(self.questions)

        self.topic_label.pack_forget()
        self.trig_button.pack_forget()
        self.algebra_button.pack_forget()

        self.next_question()

    def next_question(self):
        if self.questions:
            self.current_question = random.choice(self.questions)
            self.questions.remove(self.current_question)
            self.question_label.config(text=self.current_question["question"])
            self.entry.delete(0, tk.END)
            self.result_label.config(text="")
        else:
            self.show_score()

    def check_answer(self):
        user_answer = self.entry.get()
        correct_answer = self.current_question["answer"]
        if user_answer == correct_answer:
            self.result_label.config(text="Correct!", fg="green")
            self.correct_answers += 1
        else:
            self.result_label.config(text=f"Incorrect! The correct answer is: {correct_answer}", fg="red")

    def show_score(self):
        self.question_label.config(
            text=f"Study session complete. You answered {self.correct_answers} out of {self.total_questions} questions correctly.")
        self.entry.pack_forget()
        self.submit_button.pack_forget()
        self.result_label.pack_forget()
        self.next_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
# Uncomment the line below to run the study session
run_study_session()

