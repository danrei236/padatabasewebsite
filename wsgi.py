#from app import create_app

#if __name__ == "__main__":
 #   app.run(debug=True)

 web: gunicorn app:app
