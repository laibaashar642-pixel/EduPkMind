from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from courses.models import Courses
from users.models import User
import uuid
from certificates.models import Certificates

def generate_certificate(request, course_id):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    course = Courses.objects.get(id=course_id)

    # Certificate database mein save karo
    cert = Certificates.objects.create(
        user=user,
        course=course,
        unique_id=str(uuid.uuid4())[:8]
    )

    # PDF banao
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{cert.unique_id}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Certificate content
    p.setFont("Helvetica-Bold", 36)
    p.drawCentredString(width/2, height-150, "Certificate of Completion")

    p.setFont("Helvetica", 24)
    p.drawCentredString(width/2, height-250, f"This certifies that")

    p.setFont("Helvetica-Bold", 28)
    p.drawCentredString(width/2, height-310, user.username)

    p.setFont("Helvetica", 24)
    p.drawCentredString(width/2, height-370, "has successfully completed")

    p.setFont("Helvetica-Bold", 28)
    p.drawCentredString(width/2, height-430, course.title)

    p.setFont("Helvetica", 16)
    p.drawCentredString(width/2, height-500, f"Certificate ID: {cert.unique_id}")

    p.setFont("Helvetica", 16)
    p.drawCentredString(width/2, height-540, "EduMind - 2026")

    p.showPage()
    p.save()

    return response