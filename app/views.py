from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string

def accept(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        linkedin = request.POST.get('linkedin')
        github = request.POST.get('github')

        objective = request.POST.get('objective')

        degree = request.POST.get('degree')
        college = request.POST.get('college')
        university = request.POST.get('university')
        cgpa = request.POST.get('cgpa')
        passing_year = request.POST.get('passing_year')

        skills = request.POST.get('skills')

        projects = request.POST.get('projects')

        experience = request.POST.get('experience')

        certifications = request.POST.get('certifications')

        achievements = request.POST.get('achievements')

        languages = request.POST.get('languages')

        profile = Profile(

            name=name,
            email=email,
            phone=phone,
            address=address,

            linkedin=linkedin,
            github=github,

            objective=objective,

            degree=degree,
            college=college,
            university=university,
            cgpa=cgpa,
            passing_year=passing_year,

            skills=skills,

            projects=projects,

            experience=experience,

            certifications=certifications,

            achievements=achievements,

            languages=languages

        )

        profile.save()

    return render(request, 'app/accept.html')


def resume(request, id):

    profile = Profile.objects.get(id=id)

    html = render_to_string('app/resume.html', {'profile': profile})

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    pdf = pdfkit.from_string(html, False, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    return response


def list(request):

    profiles = Profile.objects.all()

    return render(request, 'app/list.html', {'profiles': profiles})