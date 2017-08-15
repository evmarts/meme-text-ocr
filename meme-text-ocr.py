from PIL import Image
import os
import sys
import subprocess
import tempfile
import shlex

tesseract_cmd = 'tesseract'

def give_temp_name():
    tmpfile = tempfile.NamedTemporaryFile(prefix="tess_")
    return tmpfile.name

def del_file(filename):
    try:
        os.remove(filename)
    except OSError:
        pass

def run_tesseract(input_filename, output_filename_base, lang=None):
    command = [tesseract_cmd, input_filename, output_filename_base]

    if lang is not None:
        command += ['-l', lang]

    proc = subprocess.Popen(command, stderr=subprocess.PIPE)
    status = proc.wait()
    error_string = proc.stderr.read()
    proc.stderr.close()
    return status, error_string

def image_to_string(image):
	if len(image.split()) == 4:
		r,g,b,a = image.split()
		image = Image.merge("RGB", (r,g,b))

	input_file_name = '%s.bmp' % give_temp_name()
	output_file_name_base = give_temp_name()
	output_file_name = '%s.txt' % output_file_name_base
	try:
		image.save(input_file_name)
		status, error_string = run_tesseract(input_file_name,output_file_name_base,lang = 'eng')

		f = open(output_file_name, 'rb')
		try:
			return f.read().decode('utf-8').strip()
		finally:
			f.close()
	finally:
		del_file(input_file_name)
		del_file(output_file_name)

def spell_check(text):
	text = text.replace(" u ", " you ").replace(' ur ', ' your ')
	text = text.replace(text[0], text[0].upper(), 1)
	return text

def main():
	filename = "in/" + raw_input("Image of text to recognize: in/")
	image = Image.open(filename)
	text = image_to_string(image)
	text = text.replace('\n',' ').lower()
	text = spell_check(text)
	print "Text recognized as: '" + str(text) + "'"

main()