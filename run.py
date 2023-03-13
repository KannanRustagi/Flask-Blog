from flaskblog import app

#only true if we run the application directly with python, we don't have to keep settimg the environment variables again and again
if __name__=='__main__':
    app.run(debug=True)