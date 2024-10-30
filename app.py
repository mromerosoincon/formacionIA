from flask import Flask, render_template

app = Flask(__name__)

# Semanas desbloqueadas
semanas_desbloqueadas = [1,2,3,4]  # Solo la semana 1 está desbloqueada al inicio

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tareas')
def tareas():
    return render_template('tareas.html', semanas_desbloqueadas=semanas_desbloqueadas)

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

if __name__ == '__main__':
    app.run(debug=True)
