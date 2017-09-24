#main.py
#2017, Geoffrey Hadler

from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)       #instantiate Flask
app.config['DEBUG'] = True  #enable debugging

page_template = """
<!doctype html>
<html>
    <head>
        <title>Web Caesar</title>
        <style>
            body {{
                background-color: #000;
            }}
            form {{
                background-color: #ccc;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            footer {{
                font-size: 10px;
                color: #0f0;
                text-align:right;
            }}
            .errSpan {{
                background-color: #f00;
                color: #ff0;
            }}
        </style>
    </head>
    <body>
        <main>
            <section>
                <form method="POST">
                        <label for="rot">
                            Rotate By:
                        </label>
                        <input type="text" name="rot" value="{user_rot}"/><span class="errSpan">{rot_error}</span><br/>
                        <textarea name="text">{user_text}</textarea>
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
    return page_template.format(user_rot="0",rot_error ="", user_text="")

@app.route("/", methods=['POST'])
def encrypt():
    #TODO sanitize strings
    locText = ""  
    locRot = 0
    locText = request.form['text']
    strLocRot = request.form['rot']
    strRotError = ""

    try:
        locRot = int(strLocRot)
    except:
        strRotError = "&larr;Invalid ROTation!"
        return page_template.format(user_rot=strLocRot, rot_error = strRotError,user_text=locText)    

    strEncrypt = rotate_string( locText, locRot )
    return page_template.format(user_rot=strLocRot, rot_error = strRotError,user_text=strEncrypt)


if __name__ == "__main__":
    app.run()       #call run on Flask object instance app
