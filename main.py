# IMPORTING PACKAGES :
from pypdf import PdfReader
import pyttsx3

# SETTING THE VOICE ENGINE :
engine = pyttsx3.init()

# CUSTOMISING VOICE OF THE ENGINE :
voices = engine.getProperty('voices')
# CHANGING INTO FEMALE VOICE :
engine.setProperty('voice', voices[1].id)
# SLOWS DOWN THE SPEED :
engine.setProperty('rate', 150)

# CALLBACK FUNCTION :
def on_finish(name,completed):
    if completed:
        print(f"Finished reading: {name}")
    if not completed:
        print("The reading was interrupted.")

# REQUIRED VARIABLES :
pdf_name = "sample.pdf"
with open(pdf_name, "rb") as file:
    # READING PDF :
    reading_pdf = PdfReader(file)
    pages = reading_pdf.pages

    # EXTRACTING TEXT FROM PAGES :
    page_data = [page.extract_text() for page in pages]

    # CONNECT THE CALLBACK FUNCTION TO THE EVENT :
    engine.connect("finished-utterance", on_finish)

    # CONVERTING TEXT INTO SPEECH  FROM PDF :
    for index, page in enumerate(page_data):
        clean_text = page.strip() if page else ""

        if clean_text:
            print(f"📖 Reading Page {index + 1}...")
            engine.say(clean_text, name=f"Page {index + 1}")
            engine.runAndWait()
        else:
            print(f"⏭️ Skipping Page {index + 1} (No readable text)")

    print("✅ all readable pages have been processed.")

