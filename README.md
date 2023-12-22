# FastApiProject
Fast API Project for a Patient Image Management Application


Project Description:
1.	Application server will host the:
  a.	Controller layer: REST GET API with query parameters of patient_name, patient_dob, image_captured_date
  b.	Service layer: Logic to Validate and filter the provided inputs.
  c.	User-Interface layer: Logic to display the image and metadata.
2.	Client will be a web form page to accept the patient_name, patient_dob, image_captured_date inputs.


Client Page:
1.	The Client page is currently html with form page fields.
  a.	Patient Name. (required)
  b.	Patient Date of Birth. (required)
  c.	Patient Image Captured Date. (required)

Application Server:
1.	The images are currently present as static files in the codebase. The metadata is present as Objects in the application server
2.	For a Real-Time Application, there are 3 options due to the tradeoffs to consider when deciding the location to host images:
  a.	Trade-off on Data Security, Prioritize on lowest Application latency: Store the images in the file-system, and store the metadata in Database. (postgres)
  b.	Trade-off on Database Load, Prioritize Data Security: Store the images as BLOB data in Postgres database including the metadata of the images.
  c.	There is another option to store the images in Google Cloud, and store the metadata reference of image in database. (postgres).

Instructions to run the application in a Terminal:
1.	To start the application, Run the command in terminal:
  a.	Mac, Linux: {Project Downloaded Path}/fastApiProject/.venv/bin/python -m uvicorn main:app –reload
  b.	Windows: {Project Downloaded Path}\fastApiProject\.venv\bin\python -m uvicorn main:app –reload
2.	Now after starting the application, To use the application: Open a web browser and enter the URL: http://127.0.0.1:8000/

To-Do Items:
1.	In the back-end, Update field inout to regular readable data, needs to add parsing logic and remove spaces. – JimJones -> Jim Jones
2.	In the back-end, create a new service.py file to add the input validation/filtering logic. The idea is to keep the Service layer separate to the Controller API layer.
3.	In the back-end, create a separate home.py for serving UI (html/JavaScript) logic, The idea is to keep the User-Interface layer separate to the Controller API layer.
4.	In the Client UI logic, Add better validation for each field.

Demo Recording:
1.	In the project directory.
