from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def my_form():
    website = '''
<!DOCTYPE html>
<html>
<body>
    <h1>Temperature Convertor</h1>
    
    <form action="/" method="POST">
        <label for="tempInCelsius">Celsius temperature:</label>
        <input type="text" name="tempInCelsius">
        <input type="submit" value="Convert to Fahrenheit">
    </form>
</body>
</html>'''
    return website

@app.route('/', methods=['POST'])
def my_form_post():
    celsiusTemp = request.form['tempInCelsius']
    try:
        celsiusTemp = float(celsiusTemp)

        fahrenheitTemp = celsiusTemp * 9.0/5 + 32
        return str(fahrenheitTemp)
    except:
        return "That's not a number!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
