# Codeclause-task3
Artificial intelligence 

NLP-Powered Legal Document Analyzer

This project scans a legal document and extracts key clauses such as Termination, Fees and Payment, Confidentiality, and Governing Law using Python.


---

How it works

1. The program reads the input file agreement.txt.


2. It searches for keywords (like terminate, fee, confidential, law) in each sentence.


3. For every match, the related clause is extracted.


4. The extracted clauses are displayed on the console and saved to task3_output.txt.




---

Requirements

Python 3

No additional libraries required (pure Python).



---

Steps to Run

1. Place the legal text file agreement.txt in the same folder as the script.


2. Run the script:

python task3_legal_nlp.py


3. The extracted clauses will be displayed in the console and saved to task3_output.txt.




---

Example Input (agreement.txt)

This Agreement is governed by the laws of India. Either party may terminate this Agreement if the other party breaches its obligations. Client must pay all fees within thirty (30) days. Both parties agree to maintain confidentiality of all shared information.


---

Example Output

Console Output:

Extracted Clauses:

Termination: Either party may terminate this Agreement if the other party breaches its obligations.
Fees and Payment: Client must pay all fees within thirty (30) days.
Confidentiality: Both parties agree to maintain confidentiality of all shared information.
Governing Law: This Agreement is governed by the laws of India.

task3_output.txt:

Termination: Either party may terminate this Agreement if the other party breaches its obligations.
Fees and Payment: Client must pay all fees within thirty (30) days.
Confidentiality: Both parties agree to maintain confidentiality of all shared information.
Governing Law: This Agreement is governed by the laws of India.
