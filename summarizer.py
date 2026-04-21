import tkinter as tk
from tkinter import filedialog,messagebox

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import nltk 
nltk.download('punkt')

nltk.data.path.append('C:/Users/mnum/AppData/Roaming/nltk_data')

# file path (input file)
file_path =""
# function to upload file
def upload_file():
    global file_path
    file_path=filedialog.askopenfilename(filetypes=[("Text Files","*.txt")])
    if file_path:
        file_label.config(text="File selected")
# Function to Summarize
def Summarize_text():
    if not file_path:
        messagebox.showerror("Error","Please upload a file first!")
        return
    try:
        Parser=PlaintextParser.from_file(file_path,Tokenizer("english"))
        summarizer=LexRankSummarizer()
        summary=summarizer(Parser.document,5)

        output_text.delete(1.0,tk.END)
        for sentence in summary:
            output_text.insert(tk.END,str(sentence) + "\n")
    except Exception as e:
        messagebox.showerror("Error",str(e))

#GUI setup
root=tk.Tk()
root.title("Smart city Document Summarizer")
root.geometry ("600x400")

title_label =tk.Label(root, text="AI Document Summarizer",font=("Arial",16))
title_label.pack(pady=10)

upload_btn=tk.Button(root,text='Uploaded File',command=upload_file)
upload_btn.pack(pady=5)

file_label =tk.Label(root,text="No file selected")
file_label.pack()

summarize_btn=tk.Button(root,text="Summarize",command=Summarize_text)
summarize_btn.pack(pady=10)

output_text=tk.Text(root,height=10,width=70)
output_text.pack(pady=10)

root.mainloop()