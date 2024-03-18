from reportlab.platypus import Table, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


def details(input):
    # Creating Headings

    styles = getSampleStyleSheet()
    styleN = styles["Normal"]
    paragraph_styles = ParagraphStyle('centered', parent=styleN, alignment=1)
    heading = Paragraph('<b>DAILY LESSON PLAN</b>', paragraph_styles)

    # Creating Table for Heading

    data = [[heading]]
    heading_table = Table(data)
    table_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')])
    heading_table.setStyle(table_style)

    right_heading_details_table = [
        'Date', 
        'Year', 
        'Time', 
        'Number of Pupils', 
        'Lesson', 
        'Main Skill Focus', 
        'Theme',
        'Topic', 
        'Language/ Grammar Focus', 
        'Content Standard', 
        'Content Standard', 
        'Learning Standard', 
        'Learning Standard', 
        'Learning Objectives', 
        'Success Criteria', 
        'School-based Assessment', 
        'HOTs', 
        'Cross-Curriculum (CCE)', 
        'Inculcation of Values/ Moral Values', 
        'Resources/ Teaching Aids', 
        '21st CL Activities', 
        '21st CLS Method', 
        'Soft skills', 
        'Practicum Theme'
        ]

    data = []

    for index, i in enumerate(right_heading_details_table):
        if index == 2:
           data_child = [
            Paragraph(f'<b>{i}</b>'), 
            Paragraph(f'{input[index][0]} - {input[index][1]}'), 
            Paragraph(''), 
            Paragraph(''),
            ]
        elif index == 9 or index == 10 or index == 11 or index == 12:
            data_child = [
            Paragraph(f'<b>{i}</b>'), 
            Paragraph(f'{input[index][0]}'), 
            Paragraph(f'{input[index][1]}'), 
            Paragraph(f'{input[index][2]}'),
            ]
        elif index == 13 or index == 14:
            insert_input = '<br />'.join(f'{i+1}. {item}' for i, item in enumerate(input[index]))
            data_child = [
            Paragraph(f'<b>{i}</b>'), 
            Paragraph(f'By the end of the lesson, pupils should be able to: <br /> <br /> {insert_input}'), 
            Paragraph(''),
            Paragraph('+'),
            ]
        elif index == 18 or index == 19:
            insert_input = ', '.join(f'{item}'for item in input[index])
            data_child = [
            Paragraph(f'<b>{i}</b>'), 
            Paragraph(insert_input), 
            Paragraph(''), 
            Paragraph(''),
            ]
        else :
            data_child = [
                Paragraph(f'<b>{i}</b>'), 
                Paragraph(f'{input[index]}'), 
                Paragraph(''), 
                Paragraph('')
                ]
        data.append(data_child)

    details_table_styles = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                                       ('Align', (0, 0), (-1, -1), 'LEFT'),
                                       ('SPAN', (0, 9), (0, 10)),
                                       ('SPAN', (0, 11), (0, 12)),
                                       ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                       ])

    reference = [2, 9, 10, 11, 12, 13, 14, 17, 18]
    for i in range(24):

        if i not in [9, 10, 11, 12]:
            details_table_styles.add('SPAN', (1, i), (3, i))

    colWidths = [100, 60, 60, 210]
    details_table = Table(data, colWidths=colWidths)
    details_table.setStyle(details_table_styles)

    return heading_table, details_table
