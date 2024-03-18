from django.urls import path
from . import views

data = {
    'url': [
      'view_pdf_DSKPYEAR1/',
      'view_pdf_DSKPYEAR2/',
      'view_pdf_DSKPYEAR3/',
      'view_pdf_DSKPYEAR4/',
      'view_pdf_DSKPYEAR5/',
      'view_pdf_DSKPYEAR6/',
      'view_pdf_SOWYEAR1/',
      'view_pdf_SOWYEAR2/',
      'view_pdf_SOWYEAR3/',
      'view_pdf_SOWYEAR4/',
      'view_pdf_SOWYEAR5/',
      'view_pdf_SOWYEAR6/',
      'view_pdf_TEXTBOOKYEAR1/',
      'view_pdf_TEXTBOOKYEAR2/',
      'view_pdf_TEXTBOOKYEAR3/',
      'view_pdf_TEXTBOOKYEAR4/',
      'view_pdf_TEXTBOOKYEAR5/',
      'view_pdf_TEXTBOOKYEAR6/',
      ],
    'method': [
      views.RenderPdfDSKP.view_pdf_DSKPYEAR1,
      views.RenderPdfDSKP.view_pdf_DSKPYEAR2,
      views.RenderPdfDSKP.view_pdf_DSKPYEAR3,
      views.RenderPdfDSKP.view_pdf_DSKPYEAR4,
      views.RenderPdfDSKP.view_pdf_DSKPYEAR5,
      views.RenderPdfDSKP.view_pdf_DSKPYEAR6,
      views.RenderPdfSOW.view_pdf_SOWYEAR1,
      views.RenderPdfSOW.view_pdf_SOWYEAR2,
      views.RenderPdfSOW.view_pdf_SOWYEAR3,
      views.RenderPdfSOW.view_pdf_SOWYEAR4,
      views.RenderPdfSOW.view_pdf_SOWYEAR5,
      views.RenderPdfSOW.view_pdf_SOWYEAR6,
      views.RenderPdfTEXTBOOK.view_pdf_TEXTBOOKYEAR1,
      views.RenderPdfTEXTBOOK.view_pdf_TEXTBOOKYEAR2,
      views.RenderPdfTEXTBOOK.view_pdf_TEXTBOOKYEAR3,
      views.RenderPdfTEXTBOOK.view_pdf_TEXTBOOKYEAR4,
      views.RenderPdfTEXTBOOK.view_pdf_TEXTBOOKYEAR5,
      views.RenderPdfTEXTBOOK.view_pdf_TEXTBOOKYEAR6,
    ]  
}

urlpatterns = [
    path(data["url"][i], data['method'][i], name=f"{data['url'][i]}")
    for i in range(len(data['url']))
]
