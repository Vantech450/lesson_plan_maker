from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet


def reflection():

    styles = getSampleStyleSheet()
    styleN = styles["Normal"]
    paragraph_styles = ParagraphStyle('centered',  parent=styleN, alignment=1)
    reflection_text = Paragraph('<b>Reflection</b>', paragraph_styles)

    data = ['Strengths:', 'Weaknesses:', 'Improvement:']
    data_contents = []

    for i in data:
        contents_text = Paragraph(f'{i}')
        data_contents.append([contents_text])
        for j in range(6):
            data_contents.append([''])

    table_styles = TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')])

    for i in range(len(data_contents)):
        if i not in [0, 6, 7, 13, 14]:
            table_styles.add('LINEBELOW', (0, i), (-1, i), 1, colors.black)

    table = Table(data_contents, colWidths=430)
    table.setStyle(table_styles)

    return reflection_text, table
