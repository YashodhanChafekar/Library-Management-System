from flask import Flask
from Library import library

app = library()
print("I am the best.")
print(app)

if __name__ == '__main__':
    app.run(debug=True)
    