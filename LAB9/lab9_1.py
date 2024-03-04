from flask import Flask
app = Flask(__name__)

@app.route('/cal/<opt>/<float:a>/<float:b>')

def cal(opt,a,b): 
    if opt == 'add':
        ans = a + b
        return f'<h3>{a} + {b} = {ans}</h3>'
        
    elif opt == 'sub':
        ans = a - b
        return f'<h3>{a} - {b} = {ans}</h3>'
    
    elif opt == 'mul':
        ans = a * b
        return f'<h3>{a} * {b} = {ans:.2f}</h3>'
        
    elif opt == 'div':
        if b == 0 :
            return f'<h3>{a} / {b} = {"can not div by zero"}</h3>'           
        ans = a / b
        return f'<h3>{a} / {b} = {ans:.2f}</h3>'
        
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port ='80')