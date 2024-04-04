from flask import Flask,redirect,url_for,render_template,request
from transformers import pipeline


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html',data=None)
@app.route('/',methods=['POST','GET'])
def summarize():
     if request.method=='POST':
        text=request.form['text']
        summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf") # 892M
        summary=summarizer(text, min_length=100, max_length=3000)
        data = {'message':summary[0]['summary_text']}
        return render_template('index.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)
