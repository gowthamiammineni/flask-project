from flask import Flask

AI=Flask(__name__)

@AI.route('/wish')
def wish():
    return 'This is my first flask view function'
@AI.route('/second')
def second():
    return 'This is my 2nd view function'

if __name__=='__main__':
    AI.run(debug=True,host='192.168.190.1',port=5001)