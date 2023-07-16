from flask import Flask, request, render_template
from flask_cors import CORS
from reportlab.pdfgen.canvas import Canvas
from segno import helpers
import os

app = Flask(__name__)
cors = CORS(app)

def GetQR(name ,email ,phone):
    qrcode = helpers.make_mecard(
        name=name,
        email=email,
        phone=phone
    )
    qrcode.save(name+'.png', scale=5)


def GetPdf(userName):

    canvas_width = 600
    canvas_height = 800
    can = Canvas("static/users/"+userName + ".pdf", pagesize=(canvas_width, canvas_height))
    # Calculate the center coordinates for the image
    image_width = 350
    image_height = 350
    x_start = (canvas_width - image_width) / 2
    y_start = (canvas_height - image_height) / 2 + 200

    # Draw the QR image on the canvas
    can.drawImage(
        userName+".png",
        x_start,
        y_start,
        width=image_width,
        height=image_height,
        preserveAspectRatio=True,
        mask='auto',

    )

    # Save and show the PDF

    can.save()


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/createQr", methods=["post"])
def generateQR():
    if request.method == "POST":
        jsonData = request.get_json()
        name = jsonData[0]['Fname']+" "+jsonData[0]['Lname']
        phone=jsonData[0]['phoneNumber']
        email=jsonData[0]['email']


    # Generate the QR code
    GetQR(name,email,phone)


    # Generate the PDF
    GetPdf(name)
    os.remove(name+".png")
    return {'filename': name+'.pdf'}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
