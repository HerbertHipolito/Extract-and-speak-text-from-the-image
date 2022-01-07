# -*- coding: utf-8 -*-
import pytesseract
import pyttsx3 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'      

class SpeakingText():

    def __init__(self,string,language,rate_word=200,show=True):

        self.string=string
        self.letter_list= [letter for letter in string]
        self.show=show
        self.language=language
        self.rate=rate_word

    def removing_all_symbols(self):

        for index in range(len(self.symbols)):
            self.remove_one_symbol(self.symbols[index])    

    def remove_one_symbol(self,symbol):
        
        #Receive a list. Remove the desired characters in the same order in the 'symbol'.
        
        condition = True
        
        for index in range(len(self.letter_list)-len(symbol)):

            for index2 in range(len(symbol)):
                condition = self.letter_list[index+index2] == symbol[index2]
                if not condition:
                    break
            
            if condition:
                for j in range(len(symbol)):
                    self.letter_list.pop(index)
                self.remove_one_symbol(symbol)
                
                break

    def set_symbols(self,symbols):
        self.symbols=symbols

    def set_rate_word(self,rate):
        self.rate=rate
        
    def get_string(self):
        letters=""
        for letter in self.letter_list:
            letters+=letter
        return letters

    def SpeakText(self,command):
        #Check if the language chosen to speak was installed properly and speak the received text. 
        engine = pyttsx3.init()
        number= -1
        
        for index,voice in enumerate(engine.getProperty('voices')):
            if self.language in voice.name:
                number = index
        if number == -1:
            print('The language was not recognized, check if your system has it installed in the language settings.')
            return None
        
        engine.setProperty("voice", engine.getProperty('voices')[number].id)
        engine.setProperty('rate', self.rate)
        engine.say(command)
        engine.runAndWait()
    

#text=SpeakingText(pytesseract.image_to_string(r'C:\Users\Usuario\Desktop\projetos paralelos\image_english\text3.png'),'English',140)
#print(text.get_string())
#text.SpeakText(text.get_string())
