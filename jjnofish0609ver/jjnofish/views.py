from django.shortcuts import render, redirect
from django.http import HttpResponse
from .project import main
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User
from .models import UploadedDocument
from django.http import JsonResponse


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("jj_no_fish"))
        else:
            return render(request, "jjnofish/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "jjnofish/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "jjnofish/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "jjnofish/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "jjnofish/register.html")


def jj_no_fish(request):
    upload_completed = False

    if request.method == 'POST':
        action = request.POST.get('action')
        context = main(action, request)

        if action == 'Upload & Replace':
            return render(request, 'jjnofish/jj_no_fish.html', context)

        elif action == 'Export':
            modified_doc = context.get('modified_doc')
            new_file_name = context.get('new_file_name')

            response = HttpResponse(modified_doc, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
            return response

    return render(request, 'jjnofish/jj_no_fish.html', {'upload_completed': upload_completed, 'old_word': '', 'new_word': ''})

# def UploadedDocument():
#     return models.Model(
#         'UploadedDocument',
#         document=models.FileField(upload_to='documents/'),
#         modified_document=models.FileField(upload_to='modified_documents/', blank=True, null=True)
#     )


# def jj_no_fish(request):
#     upload_completed = False

#     if request.method == 'POST':
#         action = request.POST.get('action')

#         if action == 'Upload & Replace' and 'document' in request.FILES:
#             old_words = request.POST.getlist('old_word')
#             new_words = request.POST.getlist('new_word')
#             case_sensitive = 'caseSensitive' in request.POST
#             word_pairs = list(zip(old_words, new_words))

#             context = main(action, request, word_pairs, case_sensitive)
#             return render(request, 'jjnofish/jj_no_fish.html', context)

#         elif action == 'Export':
#             modified_doc = context.get('modified_doc')
#             new_file_name = context.get('new_file_name')

#             response = HttpResponse(modified_doc, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#             response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
#             return response

#     return render(request, 'jjnofish/jj_no_fish.html', {'upload_completed': upload_completed, 'old_word': '', 'new_word': ''})


#===========backup===============

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import UploadedDocument
# from io import BytesIO
# from docx import Document
# from django.core.files.base import ContentFile

# def jj_no_fish(request):
#     upload_completed = False

#     if request.method == 'POST':
#         action = request.POST.get('action')

#         if action == 'Upload & Replace':
#             new_document = UploadedDocument(document=request.FILES['document'])
#             new_document.save()

#             old_word = request.POST.get('old_word', '')
#             new_word = request.POST.get('new_word', '')
#             replace_words_in_document(new_document.document, old_word, new_word)
#             upload_completed = True
#             return render(request, 'jj_no_fish.html', {'upload_completed': upload_completed, 'old_word': old_word, 'new_word': new_word})


#         elif action == 'Export':
#             uploaded_doc = UploadedDocument.objects.last()
#             modified_doc = replace_words_in_document(uploaded_doc.document, '', '')  # Replace with empty strings for export
#             file_name = uploaded_doc.document.name
#             if file_name.count('_') > 1:
#                 file_name_parts_right = file_name.rsplit('.', 1)[-1]
#                 file_name_parts_left = file_name.rsplit('.', 1)[0].rsplit('_', 1)[0]
#                 new_file_name = file_name_parts_left + '_modified.' + file_name_parts_right  # Append '_modified' to the file name
#             else:
#                 file_name = uploaded_doc.document.name
#                 file_name_parts = file_name.rsplit('.', 1)
#                 new_file_name = file_name_parts[0] + '_modified.' + file_name_parts[1]
#             response = HttpResponse(modified_doc, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#             response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
#             return response

#         elif action == "{% url 'jj_no_fish' %}":
#             upload_completed = False
#             return render(request, 'jj_no_fish.html', {'upload_completed': upload_completed, 'old_word': '', 'new_word': ''})

#         # After processing the form data, redirect to the same view (GET request)
#     return render(request, 'jj_no_fish.html', {'upload_completed': upload_completed, 'old_word': '', 'new_word': ''})




# def replace_words_in_document(document_file, old_word, new_word):
#     doc = Document(document_file)

#     for paragraph in doc.paragraphs:
#         if old_word in paragraph.text:
#             paragraph.text = paragraph.text.replace(old_word, new_word)

#     modified_document = BytesIO()
#     doc.save(modified_document)
#     modified_document.seek(0)

#     return modified_document.getvalue()


# def home(request):
#     return render(request, 'jj_no_fish.html', {'upload_completed': False})  # Ensure initial status is False when rendering the page
