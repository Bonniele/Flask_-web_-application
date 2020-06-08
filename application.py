'''Flask Web Application'''

from flask import Flask, render_template
from views import x, y
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.register_blueprint(x)
app.register_blueprint(y)

    
if __name__ == "__main__":
    app.run(debug=True)