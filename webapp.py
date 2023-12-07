from flask import Flask, render_template, request, redirect, url_for
import requests, glob, jinja2, os


app = Flask(__name__)
app.config['SECRET_KEY'] = '598bbob5972ax'


@app.route("/")
def home():
    welcome_message = "Welcom to Amit's website"
    list_of_names = ["Amit", "Einat", "Ella"]
#     for name in list_of_names:
#          print(name)
    return render_template("index.html", welcome_message=welcome_message, list_of_names=list_of_names)


@app.route("/content")
def content_message():
    content_on_screen_msg = "Task A:  Returns the content of any txt file and status code 200"
    path = "s*/*.txt"
    list_of_files = glob.glob(path)
    file_contents = []
    for file in list_of_files:
        with open(file, "r", encoding='utf-8') as f:
            file_content = f.read()
            file_contents.append((file, file_content))

    return render_template("content.html", content_on_screen_msg=content_on_screen_msg, list_of_files=list_of_files, file_contents=file_contents)

@app.route("/score")
def score_server():
    score_msg = "Your score is:"
    total_scores = 0
    with open('static/scores.txt', 'r') as file:
        for line in file:
            total_scores += int(line.strip())

    return render_template("scores.html", score_msg=score_msg, total_scores=total_scores)    

@app.route("/login")
def login():
     return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    register_on_screen_msg = "Task B: Writes the word “hello” into any txt file and return “success” and status code 201 as a response.\n\n Note! The action will take effect on the files within the folder: reg_form"
    form_message = "Form goes here!"
    # path = "reg*/*.txt"
    # list_of_files = glob.glob(path)
    # file_contents = []
    # for file in list_of_files:
    #     with open(file, "r+", encoding='utf-8') as f:
    #         file_content = f.write("Abra Cadabra")
    #         file_contents.append((file, file_content))

    if request.method == 'POST':
        file_name = request.form['file_name']
        folder = 'reg_form'
        path_to_file = os.path.join(folder, file_name)
        text = request.form['text']
        
        with open(path_to_file, 'a') as file:
            file.write(text + '\n')
            thankyou_message = "Your data has been submitted successfully."
            return render_template('thank_you.html', thankyou_message=thankyou_message)

    return render_template("register.html", register_on_screen_msg = register_on_screen_msg, form_message=form_message)


app.route("/thank_you")
def thank_you():
    thankyou_message = "Your data has been submitted successfully."
    return render_template("thank_you.html", thankyou_message=thankyou_message)

# ----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=30000)
     # app.run()
