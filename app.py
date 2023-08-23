<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
import os
import PyPDF2
from generate_questions import generate_interview_questions
from token_counter import num_tokens_from_messages

app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Keep track of uploaded filenames
uploaded_files = []

# Route to the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the POST request has a file part
        if 'files[]' not in request.files:
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            # If the user does not select a file, the browser sends an empty file
            if file.filename == '':
                continue

            # Save the uploaded file
            if file:
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)
                uploaded_files.append(filename)

        if len(uploaded_files) == 2:
            return redirect(url_for('view_text'))

    return render_template('index.html')

# Route to view the extracted text
@app.route('/view_text')
def view_text():
    extracted_texts = []

    for filename in uploaded_files:
        extracted_text = extract_text_from_pdf(filename)
        extracted_texts.append(extracted_text)

    candidate_text = extract_text_from_pdf(uploaded_files[1])#"\n\n".join(extracted_texts)
    job_description = extract_text_from_pdf(uploaded_files[0]) #"We are looking for a software engineer with expertise in Python and web technologies."

    generated_questions = generate_interview_questions(candidate_text, job_description)

    return render_template('view_text.html', extracted_texts=extracted_texts, generated_questions=generated_questions)
# Function to extract text from a PDF using PyPDF2
def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()
    return extracted_text

if __name__ == '__main__':
=======
from flask import Flask, render_template, request, redirect, url_for
import os
import PyPDF2
from generate_questions import generate_interview_questions
from token_counter import num_tokens_from_messages

app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Keep track of uploaded filenames
uploaded_files = []

# Route to the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the POST request has a file part
        if 'files[]' not in request.files:
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            # If the user does not select a file, the browser sends an empty file
            if file.filename == '':
                continue

            # Save the uploaded file
            if file:
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)
                uploaded_files.append(filename)

        if len(uploaded_files) == 2:
            return redirect(url_for('view_text'))

    return render_template('index.html')

# Route to view the extracted text
@app.route('/view_text')
def view_text():
    extracted_texts = []

    for filename in uploaded_files:
        extracted_text = extract_text_from_pdf(filename)
        extracted_texts.append(extracted_text)

    candidate_text = extract_text_from_pdf(uploaded_files[1])#"\n\n".join(extracted_texts)
    job_description = extract_text_from_pdf(uploaded_files[0]) #"We are looking for a software engineer with expertise in Python and web technologies."

    generated_questions = generate_interview_questions(candidate_text, job_description)

    return render_template('view_text.html', extracted_texts=extracted_texts, generated_questions=generated_questions)
# Function to extract text from a PDF using PyPDF2
def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()
    return extracted_text

if __name__ == '__main__':
>>>>>>> b6fc4fd756b59f698b9ba36ea36750d87054a22c
    app.run(debug=True)