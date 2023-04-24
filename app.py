from flask import Flask, render_template
import resume

app = Flask(__name__)

@app.route("/",methods=['GET'])
def index():
   print("hoooola")
   return render_template("index.html")

@app.route("/", methods=['POST'])
def scrape():
   url = request.form['url']
   print(url,flush=True)
   #result = resume.scrape_all(url)

   return render_template("index.html")

if __name__ == "__main__":
   app.run()