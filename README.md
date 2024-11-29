# Gas Utility Management System

A Django-based application designed for gas utility companies to efficiently handle customer service requests. This system aims to enhance the customer experience by providing an online platform to submit and track service requests while enabling customer support representatives to manage these requests effectively.

## Features

### For Customers:
- **Service Request Submission**: 
  - Customers can select the type of service request, provide detailed descriptions, and upload attachments if necessary.
- **Request Tracking**: 
  - View the status of submitted requests (Pending, In Progress, or Resolved).
  - Access timestamps for when the request was created or resolved.

## Instructions for Setup

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Vikalp1O1/gas-utility.git
   cd gas-utility
2. Set up the virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply database migrations:
   ```bash
   python manage.py migrate
5. Start the development server:
   ```bash
   python manage.py runserver

7. Navigate to http://127.0.0.1:8000/ to view the project in your browser.


## ScreenShots
### 1. Home Page
![Screenshot (1)](https://github.com/user-attachments/assets/ba182403-bac8-4442-802f-d3124a6eee86)

### 2. Signup Page
![Screenshot (2)](https://github.com/user-attachments/assets/e2a16157-1458-4412-9399-0e7d2abb7e60)

### 3. Login Page
![Screenshot (3)](https://github.com/user-attachments/assets/dac33ca5-05b4-4484-9654-dbffd1f41d85)

### 4. Home Page, After Successful login
![Screenshot (4)](https://github.com/user-attachments/assets/9da0a408-fc6b-4d24-875a-1a9eda818ecb)

### 5. Create New Request 
![Screenshot (5)](https://github.com/user-attachments/assets/91d4f524-d729-4461-9029-5b73d9124b06)

### 6. All Requests by the User
![Screenshot (6)](https://github.com/user-attachments/assets/47417d7a-3b35-4b26-8fbe-1ba984565c6e)


### Just use login id => username= user  ,  password= user1234
### Or You can Signup then login 
