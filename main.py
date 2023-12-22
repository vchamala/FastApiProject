# Author: Venkat Chamala
# Description: Endpoint file for capturing inputs, filtering, redirecting to the image display page.
# TODO: The source file currently consists of all User-Interface, Service, Controller API logic.
#  Needs to cleanly separate User-Interface, Service, Controller API layers.
#  1. Create a new ui.py file and move the User-Interface logic into the ui.py file.
#  2. Create a new service.py file and move the input validation/filtering logic into service.py file.

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from patient_images import patient_image_tuple

app = FastAPI()

# Mount the images directory to a path
app.mount("/images", StaticFiles(directory="images"), name='images')

# Home page to insert inputs.
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Image Management.</title>
        </head>
        <form action="/action_page.php" method="get">
        <label for="patient_name">Patient Full Name* :</label>
        <input type="text" id="patient_name" name="patient_name" required><br><br>
        <label for="patient_dob">Patient Date of Birth* :</label>
        <input type="text" id="patient_dob" name="patient_dob" required><br><br>
        <label for="image_captured_date">Image Captured Date* :</label>
        <input type="text" id="image_captured_date" name="image_captured_date" required><br><br>
        <button type="submit" formaction="/image/">Submit</button>
        <button type="reset">Reset</button>
        </form>
    </html>
    """

# Page to serve the image details, api method also includes filtering/validation of input data.
@app.get("/image/", response_class=HTMLResponse)
def serve(patient_name: str, patient_dob: str, image_captured_date: str):
    # we would be retrieving the image from the central DB location using a primary key..
    # primary key must be unique - so make it a mixture of name/dob/imageCapturedDate
    source = None
    message = None
    for image in patient_image_tuple:
        if patient_name == image.name and patient_dob == image.dob and image_captured_date == image.captured_date:
            source = "/images/{}-{}-{}.jpg".format(patient_name, patient_dob, image_captured_date)
            message = "Patient Name: {}, Date of Birth: {}, Image Captured Date: {}".format(patient_name,
                                                                                            patient_dob,
                                                                                            image_captured_date)
            break
    if source is None:
        source = ""
        message = "No matching image found! "
    html_display = """
    <html>
        <head>
            <title></title>
        </head>
        <body>
        <h1> {} </h1>
        <img src={}>
        <a href="/">Go to Home Page.</a>
        </body>
    </html>
    """.format(message, source)
    return html_display
