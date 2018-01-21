def export_docx(y):
    from docx import Document

    r = len(y)
    document = Document()

    document.add_heading('旋风分离器计算书', 0)
    p = document.add_paragraph('免责声明：本计算书内容由ZENLIB网站提供，其数据仅供参考，网站对此不承担任何保证责任。')

    document.add_heading('计算结果表', level=1)

    table = document.add_table(rows=r+1, cols=4)
    table.style = 'Table Grid'
    table.autofit = True
    table.cell(0, 0).text = "名称"
    table.cell(0, 1).text = "数值"
    table.cell(0, 2).text = "单位"
    table.cell(0, 3).text = "备注"
    i=1
    for key, value in y.items():
        table.cell(i,0).text = key
        table.cell(i,1).text = value
        i += 1

    document.add_page_break()

    document.save('static/results/demo.docx')


# 字典拆分成变量
def mody_01_test(x):
    for key, val in x.items():
        exec(key + '=val')
    tmp = 2
    print(locals()['T'])
    return "OK"