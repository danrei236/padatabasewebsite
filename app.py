#from app import create_app

#app = create_app()

#if __name__ == '__main__':
#    app.run()

from app import create_app
import os  # <-- Add this

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Heroku's PORT or default to 5000 locally
    app.run(host='0.0.0.0', port=port)  # <-- Bind to 0.0.0.0 and dynamic port
