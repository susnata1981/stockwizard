from main import app

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(port=8080, debug=True)