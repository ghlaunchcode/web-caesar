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
    </head>
    <body>
        <main>
            <section>
                <div id="div_caesar">
                    <form>
                        <label>
                            Rotate By:
                        </label>
                        <input type="text"/>
                        <input type="submit"/>
                    </form>
                </div>
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