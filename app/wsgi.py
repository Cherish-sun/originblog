# import os
#
# from dotenv import load_dotenv
#
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)

from originblog import create_app

app = create_app('production')

if __name__ == '__main__':
    app.run(debug=True, port=5000)