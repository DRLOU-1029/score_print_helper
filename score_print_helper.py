import fitz  # PyMuPDF
import json
import tkinter as tk

# 用户输入
original_pdf_name = '梁祝.pdf'#源文件名
new_pdf_name = '新总谱.pdf'#新文件名

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

def generate_pdf():
    # 获取用户输入
    instrument_input = instrument_text.get("1.0", tk.END).strip()
    instrument_list = instrument_input.splitlines()
    instrument_counts = {}

    for item in instrument_list:
        if ':' in item:
            name, count = item.split(':', 1)
            instrument_counts[name.strip()] = int(count.strip())

    # 转换为 JSON
    json_data = json.dumps(instrument_counts, ensure_ascii=False)
    print("Instrument counts in JSON:", json_data)

    # 生成新 PDF
    create_new_score(original_pdf_name, instrument_counts, new_pdf_name)

# 调用函数生成新 PDF
# 创建主窗口
root = tk.Tk()
root.title("乐器数量收集")

# 创建文本框
tk.Label(root, text="输入乐器名和数量（格式: 乐器名: 数量，每行一个）:").pack()

instrument_text = tk.Text(root, height=10, width=50)
instrument_text.pack()

# 创建生成按钮
generate_button = tk.Button(root, text="生成 PDF", command=generate_pdf)
generate_button.pack()

# 运行主循环
root.mainloop()