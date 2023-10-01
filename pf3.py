import os
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog

def merge_pdf():
    pdf_merger = PdfMerger()  # 实例化
    if not lst or not export_path:
        print('未选择pdf或导出路径')
        return

    for pdf in lst:  # 逐个读取需要合并的pdf文件
        with open(pdf, 'rb') as input:
            pdf_merger.append(input)

    with open(export_path[0] + '/merge.pdf', 'wb') as output:
        pdf_merger.write(output)
    print('共合并了'+str(len(lst))+'个pdf\n'+'导出为'+export_path[0] + '/merge.pdf')
def open_file():
    files = filedialog.askopenfilenames()
    if not files:return
    for file in files:
        if file[-3:] != 'pdf':continue
        if file not in chosen:
            chosen.add(file)
            lst.append(file)
            position[file] = len(lst)-1
    if lst:
        print('已经选择的文件:',lst)

def export_dir():
    ex_dir = filedialog.askdirectory()
    if export_path and ex_dir:
        export_path.pop()
    if ex_dir:
        export_path.append(ex_dir)
    if export_path:
        print('导出路径为：',export_path)

def cancel_file():
    if not lst:
        print('没有选中的文件')
        return
    files = filedialog.askopenfilenames()
    for file in files:
        if file not in position:
            continue
        position[lst[-1]] = position[file]
        lst[-1], lst[position[file]] = lst[position[file]],lst[-1]
        lst.pop()
        del position[file]
        chosen.remove(file)
    if lst:
        print('已经选择的文件:',lst)
    else:
        print('未选择文件')

if __name__ == '__main__':
    lst = []
    position = {}
    chosen = set()
    export_path = []
    window = tk.Tk()
    button = tk.Button(window, text='选择文件',command = open_file,state=tk.NORMAL)
    
    button2 = tk.Button(window, text='导出路径',command = export_dir)
    button3 = tk.Button(window, text='取消选择',command = cancel_file)
    button4 = tk.Button(window, text='合并',command = merge_pdf)

    button.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    window.mainloop()
            
