
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

# Define the document
doc = SimpleDocTemplate("curriculo_giovany.pdf", pagesize=letter)

# Define styles
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    name='TitleStyle',
    parent=styles['Heading1'],
    fontSize=16,
    textColor=colors.black,
    alignment=1,  # centered
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    name='HeadingStyle',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.blue,
    spaceBefore=12,
    spaceAfter=6,
    fontName='Helvetica-Bold'
)

subsection_style = ParagraphStyle(
    name='SubHeadingStyle',
    parent=styles['Heading3'],
    fontSize=12,
    textColor=colors.black,
    spaceBefore=6,
    spaceAfter=3,
    fontName='Helvetica-Bold'
)


normal_style = ParagraphStyle(
    name='NormalStyle',
    parent=styles['Normal'],
    fontSize=10,
    leading=12,
    spaceAfter=3,
    fontName='Helvetica'
)

contact_style = ParagraphStyle(
    name='ContactStyle',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.grey,
    fontName='Helvetica'
)


# Build the story
story = []

# Contact Information and Intro
story.append(Paragraph("<b>Giovany de Farias Lima</b>", title_style))
story.append(Paragraph("<i>Highly motivated and results-oriented professional with a background in finance and accounting, currently transitioning into the field of technology with a focus on software development and cloud computing. Eager to leverage analytical skills and financial expertise to contribute to innovative projects and solutions.</i>", normal_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Rua Silvino Lopes 480 ed Maison San Martin, João Pessoa PB", contact_style))
story.append(Paragraph("(61)98212-7644 | farias.giovany@gmail.com", contact_style))
story.append(Paragraph("<a href='http://www.linkedin.com/in/giovanylima'>LinkedIn Profile</a> | <a href='https://github.com/fariasgiovany'>GitHub Profile</a>", contact_style))


# Education Section
story.append(Paragraph("<b>FORMAÇÃO</b>", heading_style))
story.append(Paragraph("Cursando Análise e Desenvolvimento de Sistemas - UCB", normal_style))
story.append(Paragraph("Cursando Pós-Graduação em Desenvolvimento Full Stack e Cloud Computing Lato Sensu - Gran Faculdade", normal_style))
story.append(Paragraph("Pós Graduado com MBA em Finanças e Mercado Financeiro - UniCeub (2023)", normal_style))
story.append(Paragraph("Ciências Contábeis - UniCeub (2018)", normal_style))
story.append(Paragraph("Engenharias de Redes de Comunicação - UNB (interrompido)", normal_style)) #Added interrupted

# Skills Section
story.append(Paragraph("<b>COMPETÊNCIAS</b>", heading_style))
story.append(Paragraph("Programação: Python, Java, C, Matlab", normal_style)) # Consolidate programming
story.append(Paragraph("Análise de dados", normal_style))
story.append(Paragraph("Conhecimento avançado de informática", normal_style))
story.append(Paragraph("Inglês Fluente", normal_style))
story.append(Paragraph("Formado em Ciências Contábeis", normal_style))
story.append(Paragraph("Excel avançado", normal_style))
story.append(Paragraph("CRC ativo", normal_style))
story.append(Paragraph("Pacote Office avançado", normal_style)) #Consolidated Office


# Experience Section
story.append(Paragraph("<b>EXPERIÊNCIA</b>", heading_style))
story.append(Paragraph("<b>Embrapa</b> - Estagiário Contábil (2016-2018)", normal_style)) #Added bolds
story.append(Paragraph("<b>Autônomo</b> (2016-Atual)", normal_style)) #Added bolds


# Build the PDF
doc.build(story)
