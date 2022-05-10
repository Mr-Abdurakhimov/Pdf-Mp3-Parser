from pathlib import Path
import pdfplumber  # lib for working with pdf files
from gtts import gTTS  # lib for making an audio file
from art import tprint  # lib for beautiful printout the logo of our program,not necessary


def Parse_Pdf_To_Mp3(file_path, language):
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        print(f"The original file--> {Path(file_path).name}")
        print("Processing...")
        with pdfplumber.PDF(open(file_path, 'rb')) as pdf_file:
            pages = [page.extract_text() for page in pdf_file.pages]
            text = ''.join(pages)
            text = text.replace('\n', '')
        audio_file = gTTS(text, lang=language)
        audio_name = Path(file_path).stem
        audio_file.save(f"{audio_name}.mp3")
        print(f"Successfully done !")


def main():
    tprint("PDF->MP3-PARSER")
    path = input("Enter the path to a pdf file: ")
    lang = input("Choose the language : 'en' or 'ru': ")
    Parse_Pdf_To_Mp3(path, language=lang)


if __name__ == "__main__":
    main()
