import pandas as pd
from fpdf import FPDF

# Load the Excel file
df = pd.read_excel(r'C:\data\Sample3.xlsx')  # Use raw string for file path

# Define column names
COLUMN_QUESTION_NUMBER = 'Question Number'
COLUMN_QUESTION = 'Question'
COLUMN_OPTION_A = 'Option A'
COLUMN_OPTION_B = 'Option B'
COLUMN_OPTION_C = 'Option C'
COLUMN_OPTION_D = 'Option D'
COLUMN_CORRECT_ANSWER = 'Correct Answer'

# Function to clean option text
def clean_option(option):
    if isinstance(option, str):
        return option.lstrip("ABCD. ")
    return option

# Create a list to store the formatted questions
formatted_questions = []

# Validate DataFrame size
num_rows = len(df)
print(f"Number of rows: {num_rows}")

# Process rows from 2 to 61 (index 1 to 60)
for index in range(1, min(61, num_rows)):  # Ensure we do not exceed the available rows
    row = df.iloc[index]
    try:
        question_number = row[COLUMN_QUESTION_NUMBER]
        question_text = row[COLUMN_QUESTION]
        options = [row[COLUMN_OPTION_A], row[COLUMN_OPTION_B], row[COLUMN_OPTION_C], row[COLUMN_OPTION_D]]
        correct_answer = row[COLUMN_CORRECT_ANSWER]

        formatted_question = f"Question {question_number}\n{question_text}\n"
        for option_label, option_text in zip(['A', 'B', 'C', 'D'], options):
            clean_text = clean_option(option_text)
            formatted_question += f"{option_label}. {clean_text}\n"

        formatted_question += f"Correct Answer: {correct_answer}\n"
        formatted_questions.append(formatted_question)
    except KeyError as e:
        print(f"KeyError: {e} - Check column names and ensure all required columns are present.")
    except IndexError as e:
        print(f"IndexError: {e} - Check row indices and ensure they are within the DataFrame bounds.")

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Questionnaire', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create a PDF object
pdf = PDF()
pdf.add_page()

# Add each formatted question to the PDF
for question in formatted_questions:
    pdf.chapter_body(question)

# Save the PDF to a file
pdf.output('questions.pdf')
