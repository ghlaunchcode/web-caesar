#main.py
#2017, Geoffrey Hadler

from flask import Flask, request
from caesar import rotate_string

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
        </style>
    </head>
    <body>
        <main>
            <section>
                <form method="POST">
                        <label for="rot">
                            Rotate By:
                        </label>
                        <input type="text" name="rot"/><span class="ErrSpan">{rot_error}</span><br/>
                        <textarea name="text"></textarea>
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
    return page_template.format(rot_error ="")

@app.route("/", methods=['POST'])
def encrypt():
    #TODO
    #locText =   
    #locRot = 
    locRot = 7
    locText = "junk"
    strEncrypt = rotate_string( locText, locRot )
    strRet = "<h1>" + strEncrypt + "</h1>"
    return strRet

if __name__ == "__main__":
    app.run()       #call run on Flask object instance app