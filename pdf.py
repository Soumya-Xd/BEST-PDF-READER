import pyttsx3
import PyPDF2
import mpmath
import pygame
import os
from custom_voices import Speak
# import everything from sympy module
from sympy import *
import speech_recognition as sr
from tkinter.filedialog import *
Speak('LETS START')
book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

Speak = pyttsx3.init()
voices = Speak.getProperty('voices')
Speak.setProperty('voice', voices[0].id)
voicespeed = 150
Speak.setProperty('rate',voicespeed)


for num in range(0,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    Speak.say(text)
    Speak.runAndWait()

  