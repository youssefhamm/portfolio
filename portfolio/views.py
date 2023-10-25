from django.shortcuts import render
from django.http import JsonResponse
from .contact_form import ContactForm

# def index(request):
#     return render(request, 'index.html')


def inner_page(request):
    return render(request, 'inner-page.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def index(request):
    form = ContactForm()  # Initialisation du formulaire en dehors de la clause if

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistrez les données dans la base de données
            response_data = {"message": "Le formulaire a été envoyé avec succès."}
        else:
            response_data = {"message": "Une erreur s'est produite lors de l'envoi du formulaire."}
        return JsonResponse(response_data)
    return render(request, 'index.html', {'form': form})



# Cette etape permet d'envoyer un email à l'administrateur du site 

# def index(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Récupérez les données du formulaire
#             nom = form.cleaned_data['nom']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             # Envoyer l'e-mail
#             send_mail(
#                 subject,
#                 f'Nom: {nom}\nEmail: {email}\n\n{message}',
#                 'hammoujan200p@gmail.com',  # Adresse de l'expéditeur
#                 [email],  # Adresse du destinataire
#                 fail_silently=False,
#             )
#             return render(request, '/')  # Rediriger vers une page de confirmation
#     else:
#         form = ContactForm()

#     return render(request, 'index.html', {'form': form})