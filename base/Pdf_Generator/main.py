from reportlab.platypus import SimpleDocTemplate, Spacer, PageBreak
from reportlab.lib.pagesizes import A4
from .Detail import details
from .Stage import stage
from .Reflection import reflection
from .Signature import signature
from io import BytesIO
from django.http import HttpResponse

def generatepdf(data):
        buffer = BytesIO()
        
        # Configuring Imports
        heading, details_table = details(data[0])
        reflection_text, reflection_table = reflection()

        # Starting a PDF
        if '.pdf' not in data[3]:
                data[3] = data[3] + '.pdf'
        
        pdf = SimpleDocTemplate(buffer, pagesize=A4)
        flow = [
                heading, 
                Spacer(1, 20), 
                details_table, 
                PageBreak(), 
                stage(data[1]), 
                PageBreak(), 
                reflection_text,
                Spacer(1, 20), 
                reflection_table, 
                PageBreak(), 
                signature(data[2])
                ]

        # Generating PDF
        pdf.build(flow)
        
        buffer.seek(0)
        
        response = HttpResponse(buffer, content_type = 'application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{data[3]}"'
        
        return response