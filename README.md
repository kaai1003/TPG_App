### **TestProbes Guide**: Web Application ALX Portfolio Project
---

### **1. Project Name:**
**TestProbes Guide**

---

### **2. Project Description:**
The **TestProbes Guide** is a web-based application designed to assist maintenance technicians in selecting the correct test probe for testing various terminals in a wire harness. The app will have a user-friendly interface that simplifies the process of finding the right probe by inputting details such as terminal type, size, and material.

---

### **3. Project Features:**
- **Terminal Database**: A searchable database of testprobes harness terminals.
- **Interactive UI**: Frontend interface to guide technicians step-by-step through the selection process.
- **REST API**: Backend API to provide terminal data, probe compatibility, and related documentation.

---

### **4. Technologies to Be Used:**
- **Frontend**: HTML, CSS, JavaScript, jQuery
- **Backend**: Python (Flask), SQLAlchemy
- **Database**: MySQL
- **API**: RESTful API (Flask)
- **Version Control**: Git/GitHub

---


## Installation

### Prerequisites
- **Python**: Make sure Python is installed on your machine. You can download it [here](https://www.python.org/downloads/).
- **pip**: Ensure that `pip` is installed to manage Python packages.
- **MySQL**: Install MySQL or another database system if required.

### Step-by-Step Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kaai1003/TPG_App.git
   cd TPG_App
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   npm install
   ```

4. **Set Up the Database**
   - Create your database in MySQL or the required database system.
   ```bash
   mysql -u root -p < setup_TPG_DB.sql
   ```

5. **Run the Application Back-end**
   run the Back-end application:
   ```bash
   python3 app.py
   ```

6. **Run the Application Front-end**
   Finally, run the Flask application Front-end:
   ```bash
   python3 login.py
   ```

7. **Access the Application**
   - Open your browser and go to `http://localhost:5001` to access the app.
