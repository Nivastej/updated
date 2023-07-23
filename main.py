from flask import Flask, render_template , jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': "Java developer",
        'location': "remote",
        'salary': "Rs.19,00,000 LPA"
           
    },
    {
        'id': 2,
        'title': "Developer",
        'location': "Hyderabad",
        'salary': "Rs.2,00,000"
         
    },
  {
        'id': 3,
        'title': "Data scientist",
        'location': "New York"
      
         
    },
]
@app.route('/')


def home():
    return render_template('index.html',jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)
  

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
