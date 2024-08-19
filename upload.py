import os
import wx
import PyPDF2
import re
import json

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Upload .pdf, .txt, or .json")
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        pdf_button = wx.Button(panel, label="Upload PDF")
        txt_button = wx.Button(panel, label="Upload Text File")
        json_button = wx.Button(panel, label="Upload JSON File")

        pdf_button.Bind(wx.EVT_BUTTON, self.convert_pdf_to_text)
        txt_button.Bind(wx.EVT_BUTTON, self.upload_txtfile)
        json_button.Bind(wx.EVT_BUTTON, self.upload_jsonfile)

        sizer.Add(pdf_button, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(txt_button, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(json_button, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)
        self.SetSize((400, 200))

    def convert_pdf_to_text(self, event):
        with wx.FileDialog(self, "Open PDF file", wildcard="PDF files (*.pdf)|*.pdf",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            file_path = fileDialog.GetPath()
            if file_path:
                with open(file_path, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    num_pages = len(pdf_reader.pages)
                    text = ''
                    for page_num in range(num_pages):
                        page = pdf_reader.pages[page_num]
                        if page.extract_text():
                            text += page.extract_text() + " "
                    
                    text = re.sub(r'\s+', ' ', text).strip()

                    sentences = re.split(r'(?<=[.!?]) +', text)
                    chunks = []
                    current_chunk = ""
                    for sentence in sentences:
                        if len(current_chunk) + len(sentence) + 1 < 1000:
                            current_chunk += (sentence + " ").strip()
                        else:
                            chunks.append(current_chunk)
                            current_chunk = sentence + " "
                    if current_chunk:
                        chunks.append(current_chunk)
                    with open("vault.txt", "a", encoding="utf-8") as vault_file:
                        for chunk in chunks:
                            vault_file.write(chunk.strip() + "\n")
                    wx.MessageBox("PDF content appended to vault.txt", "Info", wx.OK | wx.ICON_INFORMATION)

    def upload_txtfile(self, event):
        with wx.FileDialog(self, "Open text file", wildcard="Text files (*.txt)|*.txt",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            file_path = fileDialog.GetPath()
            if file_path:
                with open(file_path, 'r', encoding="utf-8") as txt_file:
                    text = txt_file.read()
                    
                    text = re.sub(r'\s+', ' ', text).strip()

                    sentences = re.split(r'(?<=[.!?]) +', text)
                    chunks = []
                    current_chunk = ""
                    for sentence in sentences:
                        if len(current_chunk) + len(sentence) + 1 < 1000:
                            current_chunk += (sentence + " ").strip()
                        else:
                            chunks.append(current_chunk)
                            current_chunk = sentence + " "
                    if current_chunk:
                        chunks.append(current_chunk)
                    with open("vault.txt", "a", encoding="utf-8") as vault_file:
                        for chunk in chunks:
                            vault_file.write(chunk.strip() + "\n")
                    wx.MessageBox("Text file content appended to vault.txt", "Info", wx.OK | wx.ICON_INFORMATION)

    def upload_jsonfile(self, event):
        with wx.FileDialog(self, "Open JSON file", wildcard="JSON files (*.json)|*.json",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            file_path = fileDialog.GetPath()
            if file_path:
                with open(file_path, 'r', encoding="utf-8") as json_file:
                    data = json.load(json_file)

                    text = json.dumps(data, ensure_ascii=False)
                    
                    text = re.sub(r'\s+', ' ', text).strip()

                    sentences = re.split(r'(?<=[.!?]) +', text)
                    chunks = []
                    current_chunk = ""
                    for sentence in sentences:
                        if len(current_chunk) + len(sentence) + 1 < 1000:
                            current_chunk += (sentence + " ").strip()
                        else:
                            chunks.append(current_chunk)
                            current_chunk = sentence + " "
                    if current_chunk:
                        chunks.append(current_chunk)
                    with open("vault.txt", "a", encoding="utf-8") as vault_file:
                        for chunk in chunks:
                            vault_file.write(chunk.strip() + "\n")
                    wx.MessageBox("JSON file content appended to vault.txt", "Info", wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
