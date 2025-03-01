from flask import Flask
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function

@app.route('/hello')
def hello_world():
    return 'hello world!'
app.add_url_rule('/', 'hello', hello_world)


app.debug = True
app.run()
app.run(debug = True)


if __name__ == '__main__':
    app.run()

def main():

    print("Hello world! ")