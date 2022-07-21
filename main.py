from flask import Flask
from Library import library

app = library()


if __name__ == '__main__':
    app.run(debug=True)
    
