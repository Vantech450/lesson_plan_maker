from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def stage(input):
    styles_initialize = getSampleStyleSheet()['Normal']
    paragraph_styles = ParagraphStyle('centered', parent=styles_initialize, alignment=1)
    styles = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                         ('ALIGN', (0, 0), (0, 3), 'CENTER'),
                         ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
                         ('VALIGN', (0, 0), (-1, -1), 'TOP')])

    data = []

    new_data = ['Steps/ Time', 'Set Induction <br/> (5 +- mins)', 'Presentation <br/> (20 +- mins)', 'Practice <br/> (20 +- mins)',
                'Production <br/> (20 +- mins)', 'Closure <br/> (5 +- mins)']

    for index, i in enumerate(new_data):
        if i == new_data[0]:
            data.append([Paragraph(f'<b>{i}</b>', paragraph_styles),
                         Paragraph('<b>Content</b>', paragraph_styles),
                         Paragraph('<b>Teaching and Learning Activities</b>', paragraph_styles),
                         Paragraph('<b>Remarks</b>', paragraph_styles)])
        else:
            insert_data1 = '<br/>'.join(f'{i+1}. {item}'for i, item in enumerate(input[index-1][1]))
            insert_data2 = ', '.join(f'{item}'for item in input[index-1][2])
            data.append([
                Paragraph(f'<b>{i}</b>', paragraph_styles), 
                Paragraph(input[index-1][0], paragraph_styles), 
                Paragraph(insert_data1), 
                Paragraph(f'Teaching aids: {insert_data2}')
                ])

    table = Table(data, colWidths=[80, 80, 180, 90])
    table.setStyle(styles)

    return table
