from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Mm, Inches
from datetime import timedelta, date
import pytils


def insert_event(doc: Document, sight: str, body: str):
    day1_desc = doc.add_paragraph()
    runner = day1_desc.add_run(f'{sight.start_at} - {sight.end_at} - {sight.sight.title}')  
    runner.bold = False
    runner1 = day1_desc.add_run(body)
    runner1.bold = False
    runner.add_break()

def create_program_docx(trip: 'Trip'):
    doc: Document = Document()
    style = doc.styles['Normal']
    style.font.name = 'TimesNewRoman'
    style.font.size = Pt(14)
    style.font.bold=False
    section = doc.sections[0]
    section.left_margin = Mm(15)
    section.right_margin = Mm(10)
    section.top_margin = Mm(15)
    section.bottom_margin = Mm(10)

    header = doc.add_paragraph()
    runner = header.add_run('Программа')
    header.add_run().add_break()
    runner1 = header.add_run(trip.title)
    runner.font.name = runner1.font.name = 'Arial'
    runner.font.size = runner1.font.size = Pt(13)
    runner.bold = runner1.bold =True
    header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header.add_run().add_break()

    subheader = doc.add_paragraph()
    subheader.alignment = WD_ALIGN_PARAGRAPH.CENTER
    runner = subheader.add_run(f'При группе {trip.group()} чел. - 9999 руб.')
    runner.bold = True
    runner.add_break()

    days = trip.days.all()
    for i, day in enumerate(days, start=1):
        day_header = doc.add_paragraph()
        day_header.paragraph_format.space_before = Inches(0)
        day_header.paragraph_format.space_after = Inches(0)
        day_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
        runner = day_header.add_run(f'{i} день')
        runner.add_break()
        runner.bold = runner1.bold =True
        runner1 = day_header.add_run(pytils.dt.ru_strftime(u"%d %B", inflected=True, date=day.date))
        runner.bold = runner1.bold =True
        runner1.underline = True

        for sight in day.daysight_set.all():
            insert_event(doc, sight, sight.sight.description)

    doc.save(f'program_{trip.id}.docx')
