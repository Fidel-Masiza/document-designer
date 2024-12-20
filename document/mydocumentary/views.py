from django.shortcuts import render, redirect
from .models import CoverLetter

# View to list all cover letters
def cover_letter_list(request):
    # Fetch all cover letters without filtering by user
    cover_letters = CoverLetter.objects.all()
    return render(request, 'cover_letter_list.html', {'cover_letters': cover_letters})

# View to create a new cover letter
def create_cover_letter(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        job_title = request.POST['job_title']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        body = request.POST['body']
        
        cover_letter = CoverLetter(
            full_name=full_name,
            job_title=job_title,
            email=email,
            phone=phone,
            address=address,
            body=body
        )
        cover_letter.save()
        return redirect('cover_letter_list')  # Redirect to the list view
    
    return render(request, 'create_cover_letter.html')
