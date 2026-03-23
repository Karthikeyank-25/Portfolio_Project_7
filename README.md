# 🔊 PDF to Speech Converter

This project is a Python-based application that converts PDF documents into speech. It reads text from each page of a PDF file and uses a text-to-speech engine to narrate the content aloud.

This is especially useful for accessibility, audiobooks, or multitasking while reading documents.

---

## 🚀 Features

* 📄 Reads text from PDF files
* 🔊 Converts text into speech
* 🎙️ Customizable voice (male/female)
* ⏱️ Adjustable speech speed
* 📖 Reads page-by-page
* ⚡ Skips empty or unreadable pages
* 🧠 Callback function to track reading completion

---

## 🛠️ Technologies Used

* Python 🐍
* pypdf 📄
* pyttsx3 🔊

---

## 📂 Project Structure

```id="a9k2lm"
project-folder/
│
├── main.py
├── sample.pdf
└── README.md
```

---

## ⚙️ How It Works

1. Loads the PDF file using `pypdf`
2. Extracts text from each page
3. Initializes the text-to-speech engine
4. Configures:

   * Voice type (female/male)
   * Speech rate
5. Reads each page aloud sequentially
6. Skips pages with no readable text
7. Uses a callback function to confirm when reading is finished

---

## ▶️ How to Run

### 1. Clone the repository

```bash id="q1z8mx"
git clone https://github.com/your-username/pdf-to-speech.git
cd pdf-to-speech
```

### 2. Install dependencies

```bash id="w7n3lp"
pip install pypdf pyttsx3
```

### 3. Add your PDF file

* Place your PDF file in the project folder
* Update the filename in the script:

```python id="c8x2jd"
pdf_name = "sample.pdf"
```

### 4. Run the script

```bash id="v2k9rt"
python main.py
```

---

## 🧠 Example Output

```id="m5p8qa"
📖 Reading Page 1...
Finished reading: Page 1
📖 Reading Page 2...
Finished reading: Page 2
⏭️ Skipping Page 3 (No readable text)
```

---

## ⚠️ Notes

* Works only with **text-based PDFs** (not scanned images)
* Voice options depend on your system
* Large PDFs may take more time

---

## 🚀 Future Improvements

* Add GUI (Tkinter / PyQt)
* Support scanned PDFs using OCR (Tesseract)
* Save output as audio file (MP3)
* Add pause/resume functionality
* Add language selection 🌍

---

## 👨‍💻 Author

Karthikeyan

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
