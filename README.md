Smart Hire
AI-Based Resume Screening and Plagiarism Detection

Smart Hire is an AI-powered resume screening system that helps recruiters automatically analyze and rank resumes based on a job description. The system also detects similar or plagiarized resumes and extracts important candidate information such as name, email, and phone number.

This project demonstrates how Natural Language Processing (NLP) and Machine Learning techniques can be used to automate the recruitment screening process.

Features

Upload multiple resumes in PDF format

Enter a job description for candidate matching

Automatic resume text extraction

Candidate information extraction

Name

Email

Phone number

AI-based resume ranking

Plagiarism detection between resumes

Interactive candidate leaderboard

Resume preview feature

Simple web interface using Gradio

Technologies Used
Programming Language

Python

Libraries

spaCy – Natural Language Processing

PyPDF2 – PDF text extraction

scikit-learn – TF-IDF and cosine similarity

pandas – Data handling

regex – Pattern matching

gradio – Web interface

Project Workflow

User uploads multiple resume PDF files.

User enters the job description.

The system extracts text from resumes.

Important candidate information is extracted using NLP and Regex.

The job description and resumes are converted into TF-IDF vectors.

Cosine Similarity calculates how closely each resume matches the job description.

Resumes are ranked based on match score.

The system also compares resumes to detect plagiarism or high similarity.

Results are displayed in an interactive leaderboard.
