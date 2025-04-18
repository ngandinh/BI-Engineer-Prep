from flask import Flask, render_template
from plan_data import prep_plan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', prep_plan=prep_plan)

if __name__ == '__main__':
    app.run(debug=True)

