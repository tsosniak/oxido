# HTML content generator 

## Description

Based on provided text file, generate HTML conetent using OpenAI features.

---

## Requirements

This project is built with Python 3.9 and requires several dependencies. Follow the instructions below to set up and run the project locally on your Windows machine.

---

## Setup Instructions for Windows

### 1. Clone the Repository

Using terminal/CMD:<br/>

Navigate to a folder in your local machine and clone the project repository:<br/>
```git clone https://github.com/tsosniak/oxido.git```

### 2. Install python >=3.9

Ensure you have Python 3.9 or later version installed on your system.<br/>

You may be refer to [Python 3.9.10](https://www.python.org/downloads/release/python-3910/).
### 3. Create and Activate a Virtual Environment

Using termival/CMD:<br/>

Navigate to the folder where repository was cloned:
```cd <project-folder>```

Create the virtual environment:
```python -m venv venv```

Activate the virtual environment:
```venv\Scripts\activate```

### 4. Install Project Dependencies

Using terminal/CMD:<br/>
```pip install -r requirements.txt```

### 5. Rename and update .env.dev file

Inside your ```<project-folder>``` folder you can find ```.env.dev``` file. <br/>
```.env.dev``` file should be renamed to: ```.env```<br />
```your-api-key``` should be replaced by OpenAI API key

### 6. Run the Project

```python main.py```

### 7. See the output

In your ```<project-folder>``` folder you should see generated artykul.html file



