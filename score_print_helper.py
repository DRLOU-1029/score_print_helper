import fitz  # PyMuPDF
import json
import tkinter as tk
from tkinter import ttk, filedialog
# 该版本的代码是在testbak2.py的基础上进行修改的，给乐器选择框添加了默认选项和自定义乐器输入框，用户可以选择常见乐器类型或输入自定义乐器名称。
# 另外可以选择源文件名，省去输入。新文件名默认为源文件名加上“_改”.
def find_instrument_pages(original_pdf_path, instruments):
    instrument_ranges = {instrument: [] for instrument in instruments}

    # 打开原始 PDF 文件
    doc = fitz.open(original_pdf_path)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()

        for instrument in instruments:
            if instrument in text and page_num not in instrument_ranges[instrument]:
                instrument_ranges[instrument].append(page_num)

    doc.close()
    return instrument_ranges


def create_new_score(original_pdf_path, instrument_counts, new_pdf_path):
    # 找到每个乐器的页面
    instrument_ranges = find_instrument_pages(original_pdf_path, instrument_counts.keys())

    # 创建新的 PDF 文档
    new_doc = fitz.open()
    doc = fitz.open(original_pdf_path)

    for instrument, count in instrument_counts.items():
        if instrument in instrument_ranges and instrument_ranges[instrument]:
            # 获取乐器的页码
            page_nums = instrument_ranges[instrument]
            for _ in range(count):
                for page_num in page_nums:
                    new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)

    # 保存新 PDF 文件
    new_doc.save(new_pdf_path)
    new_doc.close()
    doc.close()
    print(f"New PDF created at: {new_pdf_path}")


def add_instrument():
    instrument = instrument_choice.get()
    if instrument == "其他":
        instrument = custom_instrument_entry.get().strip()
    count = int(instrument_count_entry.get().strip())

    if instrument:
        instrument_counts[instrument] = count
        instrument_listbox.insert(tk.END, f"{instrument}: {count}")
        custom_instrument_entry.delete(0, tk.END)
        instrument_count_entry.delete(0, tk.END)

def select_original_pdf():#选择源文件
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        original_pdf_entry.delete(0, tk.END)
        original_pdf_entry.insert(0, file_path)

def generate_pdf():
    # 获取文件名
    original_pdf_name = original_pdf_entry.get().strip()
    new_pdf_name = new_pdf_entry.get().strip()

    if not new_pdf_name:
        base_name = original_pdf_name.split(".")[0]
        new_pdf_name = f"{base_name}_改"
    # 检查文件名是否为空
    if not original_pdf_name:
        print("请确保源文件名已正确填写。")
        return

    # 转换为 JSON
    json_data = json.dumps(instrument_counts, ensure_ascii=False)
    print("Instrument counts in JSON:", json_data)

    # 生成新 PDF
    create_new_score(original_pdf_name, instrument_counts, new_pdf_name+'.pdf')


# 创建主窗口
root = tk.Tk()
root.title("PDF 文件生成器")

# 文件名输入框
# 源文件选择
tk.Label(root, text="源文件名:").pack()
original_pdf_entry = tk.Entry(root, width=50)
original_pdf_entry.pack()

select_pdf_button = tk.Button(root, text="选择源文件", command=select_original_pdf)
select_pdf_button.pack()

tk.Label(root, text="新文件名:").pack()
new_pdf_entry = tk.Entry(root, width=50)
new_pdf_entry.pack()

# 乐器选择框
instrument_counts = {}
tk.Label(root, text="选择乐器类型:").pack()
common_instruments = ["小提琴", "长笛2", "长笛1", "高音萨克斯chen", "吉他"]
instrument_choice = ttk.Combobox(root, values=common_instruments + ["其他"], state="readonly")
instrument_choice.pack()
instrument_choice.set("小提琴")  # 默认选项

# 自定义乐器输入框
tk.Label(root, text="如果选择其他，请输入乐器名称:").pack()
custom_instrument_entry = tk.Entry(root, width=50)
custom_instrument_entry.pack()

# 乐器数量输入框
tk.Label(root, text="输入数量:").pack()
instrument_count_entry = tk.Entry(root, width=10)
instrument_count_entry.pack()

# 添加乐器按钮
add_button = tk.Button(root, text="添加乐器", command=add_instrument)
add_button.pack()

# 显示乐器列表
instrument_listbox = tk.Listbox(root, width=50, height=10)
instrument_listbox.pack()

# 生成 PDF 按钮
generate_button = tk.Button(root, text="生成 PDF", command=generate_pdf)
generate_button.pack()

# 运行主循环
root.mainloop()