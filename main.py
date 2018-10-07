from Flask import Flask,request,redirect, render_template

app= Flask(__name__)
app.config['DEBUG']= True

tasks=[]

@app.route('/todos', methods=['POST','get'])
def index():
    if request.method =='POST':
       task = request.form('task')
       tasks.append(task)
    return render_template('todos.html',title ='ToDos',tasks=tasks)

app.run()
