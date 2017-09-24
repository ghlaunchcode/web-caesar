#main.py
#2017, Geoffrey Hadler

from flask import Flask

app = Flask(__name__)       #instantiate Flask
app.config['DEBUG'] = True  #enable debugging

page_template = """
<!doctype html>
<html>
    <head>
        <title>Web Caesar</title>
        <style>
            form {
                background-color: #ccc;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <main>
            <section>
                <form method="POST">
                        <label for="rot">
                            Rotate By:
                        </label>
                        <input type="text" name="rot"/>
                        <input type="textarea" name="text"/>
                        <input type="submit"/>
                </form>
            </section>
            <footer>
                2017, Geoffrey Hadler
            </footer>
        </main>
    </body>
</html>
"""

@app.route("/")
def index():
    return page_template

app.run()