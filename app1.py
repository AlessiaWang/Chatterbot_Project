#link to the trained bot
from Chatbot01 import bot

#load the flask framework to run web applications
from flask import Flask, render_template, request

#build a flask application 'app1'
app1 = Flask(__name__)

#write a function for 'app1' to run the Flask App as the front end of this chatbot 
@app1.route("/")
def home1():    
    return render_template("home01.html") #run the App using home01.html as template
@app1.route("/get")
def get_bot_response1():    
    userText = request.args.get('msg').strip().lower()    
    return str(bot.get_response(userText)) #show the output data in the front end from the Output given by bot.get_response(Input)
if __name__ == "__main__":    
    app1.run(host='0.0.0.0', port=3004, debug = True) #define the port as 3004 so that this App can run together with the other App in the other experimental condition