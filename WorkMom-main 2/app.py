from flask import Flask, render_template, request, Blueprint
import cohere
co = cohere.Client("api_key")
app = Blueprint('app', __name__)

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/BWTSI')
def BWTSI():
    return render_template('BWTSI.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')
   
@app.route("/response", methods=["GET", "POST"])
def generate():
   if request.method == "POST":
     prompt = request.form["prompt"]
     response = co.generate( 
            model='xlarge', 
            prompt= "Given a statement, this program will generate a professional and kind version of the sentence to give to a person of authority\n\nStatement: I am overworked\nProfessional response: I feel as though I have been given numerous tasks outside of my responsibilities\n\n--\nStatement: I cannot do this anymore\nProfessional response: I am struggling to keep up and would like to discuss different options\n\n--\nStatement: I really need to talk about my pay\nProfessional Response: Would there be an opportunity at any point to discuss my compensation?\n\n--\nStatement:{}\nProfessional Response:".format(prompt),
            max_tokens=17, #2-3 tokens in a word 
            temperature=0.5, #controls randomness
            k=0, 
            p=0.75, 
            frequency_penalty=0, 
            presence_penalty=0, 
            stop_sequences=["--"], #indicates cut off point
            return_likelihoods='NONE')
     response = response.generations[0].text
     return render_template("BWTSI.html", response = response)
        
if __name__ == "__main__":
    app.run()

    






      

           
        
              
                        


       





   

       













