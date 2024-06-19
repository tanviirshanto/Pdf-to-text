import os
os.environ["PATH"] += os.pathsep + os.pathsep.join(["Python310"])

import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract,codecs
from pdf2image import convert_from_path
from PIL import Image



if platform.system() == "Windows":

	pytesseract.pytesseract.tesseract_cmd = (
		r"Tesseract-OCR\tesseract.exe"
	)

	path_to_poppler_exe = Path(r"poppler-0.68.0\bin")
	

	out_directory = Path(r"posts").expanduser()
else:
	out_directory = Path("~").expanduser()	

pdfPath=input("\n\n\tEnter Your PDF Path:\t")
pdfPath=pdfPath.replace('"','')
language=input("\n\tEnglish = eng, Bengali = ben, Arabic = ara ( Use + for multi-language Pdf )\n\n\tEnter This PDF's Language : ")
PDF_file = Path(r"{}".format(pdfPath))

image_file_list = []

text_file = out_directory / Path("datex.txt")

def main():

	with TemporaryDirectory() as tempdir:

		if platform.system() == "Windows":
			pdf_pages = convert_from_path(
				PDF_file, 500, poppler_path=path_to_poppler_exe
			)
		else:
			pdf_pages = convert_from_path(PDF_file, 500)

		for page_enumeration, page in enumerate(pdf_pages, start=1):

			filename = f"{tempdir}\page_{page_enumeration:03}.jpg"

			page.save(filename, "JPEG")
			image_file_list.append(filename)


		with codecs.open(text_file, "a","utf-8") as output_file:

			for image_file in image_file_list:

				img=Image.open(image_file)
				text = str((pytesseract.image_to_string(img, lang=language)))

				text = text.replace("\n\n", "~~~")
				text = text.replace("\n", " ")
				text = text.replace("~~~", "\n\n")
				
				output_file.write(text)

if __name__ == "__main__":

	main()
