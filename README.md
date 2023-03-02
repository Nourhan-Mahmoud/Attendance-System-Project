# Attendance-System-Project

## How to run the project

1. run the requirements.txt file 

2. cd Attendance-System-Project\Deployment 

3. streamlit run Home_Page.py [ARGUMENTS]


## Overview fro the Application

1. ### Home page 

    First, with our face recognition app, students can simply stand in front of a camera and their faces will be scanned and matched against a pre-existing image of registered students. Once the system identifies the student, their attendance will be marked as present automatically. This app can also be integrated with student databases and course schedules, so that instructors can easily keep track of attendance in real-time. 

    Not only does this app save time and reduce the administrative burden on instructors, but it also enhances security and reduces the risk of impersonation or cheating. Additionally, the face recognition app can generate detailed reports and analytics on student attendance, providing valuable insights to educators and administrators to make informed decisions. 

    Overall, the face recognition app is a game-changing technology that can streamline attendance taking and improve the overall efficiency and effectiveness of educational institutions. 

 
![Getting Started](./7.Documentaion/home.jpeg)

2. ### Add New Student Page 

 

    Step-by-Step Description: 

    

    - The student navigates to the "Add New Student" page on the app. 

    - The student takes a picture of themselves using the camera within the app. 

    - The page displays a preview of the image, and prompts the student to confirm whether or not they want to use this image as their profile picture. 

    - the page prompts them to enter their name. 

    - The student enters their name into a text field. 

    - The app saves the image and the student's name to a server for use in the attendance phase later. 

    

    Code Overview: 

    

    The app uses OpenCV library to allow the student to take a picture. 

    The app uses facial-recognition library to detect and identify the face in the image. 

    The app saves the image file to a designated directory storage location. 

    The app prompts the student to enter their name using a text field. 

    When the student enters their name, the app saves it. 

    The app stores the image file and the associated name in a way that will allow it to be used for attendance tracking later. 

![Getting Started]r(./7.Documentaion/add_student.jpeg)


3. ### Attendance with camera Page 

 

    - The student navigates to the "Attendance With Camera" page  

    - It displays two choices: "Create New Attendance Sheet" or "View Sheets". 

    - If the student chooses to create a new attendance sheet, The student enters a name for the sheet in a text field. 

    - The app creates a new attendance sheet with the name provided by the student. 

    - If the student chooses to view created sheets, the app displays a list of previously created attendance sheets. 

    - The student selects a previously created sheet from the list using a drop-down or similar interface. and the app automatically renames the selected sheet with the current date appended to the name. 

    - The app displays two buttons: "Start Taking Attendance" and "Cancel". 

    - The code uses face recognition to scan the camera feed for faces. 

    If a student is recognized as being in the database, a rectangle box is drawn around their face with their name written above the box. 

    If a student is not recognized, a rectangle box is drawn around their face with the word "Unknown" written above the box. 

    - The code adds the student's attendance status (present/absent) to the current attendance sheet. 

    - Program continues scanning for faces and adding attendance statuses until the student clicks the "Stop Taking Attendance" button. 

    - When the student clicks the "Stop Taking Attendance" button, the app saves the current attendance sheet to a or server.


![Getting Started](./7.Documentaion/attendance_with_camera.jpeg)


4. ### Manual Attendance Page 

 

    - The student navigates to the "Manual Attendance" page  

    - There are two options: Create new attendance sheet or view created sheet. 

    - You can then Add record manually in the selected sheet 

![Getting Started](./7.Documentaion/manual_attendance.jpeg)
