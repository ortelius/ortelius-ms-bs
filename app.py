import json;
from flask import Flask

app = Flask(__name__)

@app.route('/')

def bubble_sort():
    list=[10,1,200,-19,21,321,0,200]
    for i in range (0,len(list)-1):
        for j in range(len(list)-1):
            if (list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return json.dumps(list)

if __name__ == "__main__":
    app.run(debug=True)
