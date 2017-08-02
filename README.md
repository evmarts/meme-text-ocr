# meme-text-ocr
Applies Tesseract Optical Character Recognition on an image of text taken from a meme.

### Motivation:

In a [previous project](https://github.com/evmarts/twitter-screencap-cropper), we partitioned a meme into a text component and an image component: 

<img src="./docs/sample_meme_contours.jpg" width="256px" alt="">

We may want to convert the text component into a string so that we can reuse, modify or analyze it.

### twitter-text-ocr.py

Prompts user for an image of text:

~~~
$ python twitter-text-ocr.py
Image of text to recognize: sample_text.jpg
~~~

Outputs a string:

~~~
Text: when you call shotgun but end up in the back
~~~