import fitz  # PyMuPDF
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Function to preprocess text
def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text)
    # Convert to lowercase
    tokens = [word.lower() for word in tokens]
    # Remove punctuation
    tokens = [word.translate(str.maketrans('', '', string.punctuation)) for word in tokens]
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Remove empty tokens
    tokens = [word for word in tokens if word.strip() != '']
    return ' '.join(tokens)

# Function to generate summary
def generate_summary(text, word_count=500):
    # Split the text into words
    words = text.split()
    # Initialize variables
    summary_words = []
    word_count_so_far = 0
    
    # Iterate through words and add to summary until word_count limit is reached
    for word in words:
        summary_words.append(word)
        word_count_so_far += 1
        if word_count_so_far >= word_count:
            break
    
    # Join the summary words into a single string
    summary = ' '.join(summary_words)
    
    return summary

# Main function
def main():
    pdf_path = r'C:\Users\lakshmi devi\Desktop\gowtham\4K Video\Operations Management.pdf'
    
    # Step 1: Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Step 2: Preprocess the text
    clean_text = preprocess_text(text)
    
    # Step 3: Generate summary
    summary = generate_summary(clean_text, word_count=500)
    
    print("Summary:")
    print(summary)

if __name__ == "__main__":
    main()
