# Task 3 – NLP-Powered Legal Document Analyzer
# This program extracts important clauses from legal documents using keyword search.

# Open and read the legal document
try:
    with open("agreement.txt", "r") as f:
        text = f.read()
except FileNotFoundError:
    print("Error: agreement.txt not found. Please place it in the same folder.")
    exit()

# Define the clauses and keywords to search for
clauses = {
    "Termination": ["terminate", "termination"],
    "Fees and Payment": ["fee", "payment", "invoice"],
    "Confidentiality": ["confidential", "non-disclosure"],
    "Governing Law": ["governing law", "jurisdiction", "venue"]
}

# Split the text into sentences for scanning
sentences = [line.strip() for line in text.replace("\n", " ").split(".") if line.strip()]

# Extract matching clauses
results = []
for clause_name, keywords in clauses.items():
    for sentence in sentences:
        if any(keyword in sentence.lower() for keyword in keywords):
            results.append(f"{clause_name}: {sentence}.")
            break  # take only the first matching sentence per clause

# Print and save results
if results:
    print("Extracted Clauses:\n")
    for res in results:
        print(res)

    with open("task3_output.txt", "w") as out:
        for res in results:
            out.write(res + "\n")
else:
    print("No clauses found in the document.")
