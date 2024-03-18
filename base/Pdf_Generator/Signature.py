from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors


def signature(input):
    styles = getSampleStyleSheet()["Normal"]
    paragraph_styles = ParagraphStyle('centered', parent=styles, alignment=1)
    table_styles = TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')])

    data = []
    insert_data = [["Teacher Trainee's Signature", "", "Mentor's Signature"],
                   ["", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   [f"({input[0]})", "", f"({input[1]})"],
                   ["", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   ["Headmaster's Signature", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   [f"({input[2]})", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   ["Lecturer's Signature", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   [f"({input[3]})", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   ["Lecturer's Comments", "", ""],
                   ["", "", ""],
                   ["", "", ""],
                   ["", "", ""], ]

    for i in insert_data:
        data.append([Paragraph(f'<b>{i[0]}</b>', paragraph_styles), Paragraph(f'{i[1]}', paragraph_styles), Paragraph(f'<b>{i[2]}</b>', paragraph_styles)])

    for i in range(len(data)):
        if i == 2:
            table_styles.add('LINEBELOW', (0, i), (0, i), 1, colors.black)
            table_styles.add('LINEBELOW', (2, i), (2, i), 1, colors.black)
        elif i == 10 or i == 18:
            table_styles.add('LINEBELOW', (0, i), (0, i), 1, colors.black)
        elif i in [25, 26, 27]:
            table_styles.add('LINEBELOW', (0, i), (2, i), 1, colors.black)

    table = Table(data, colWidths=[130, 170, 130], rowHeights=20)
    table.setStyle(table_styles)

    return table
