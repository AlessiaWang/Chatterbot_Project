#link to the trained bot
from Chatbot02 import bot

#load the flask framework to run web applications
from flask import Flask, render_template, request

#build a flask application 'app2'
app2 = Flask(__name__)

#write a function for 'app2' to run the Flask App as the front end of this chatbot 
@app2.route("/")
def home():    
    return render_template("home02.html") #run the App using home02.html as template
@app2.route("/get")
def get_bot_response():    
    userText = request.args.get('msg').strip().lower()    
    return str(bot.get_response(userText)) #show the output data in the front end from the Output given by bot.get_response(Input)
if __name__ == "__main__":    
    app2.run(host='0.0.0.0', port=3000, debug = True) #define the port as 3000 so that this App can run together with the other App in the other experimental condition
