from django.shortcuts import render, get_object_or_404
from django.http import Http404
from contact.models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    # Esse é o método 'convencional' de mostrar uma página não existente sem erro de index, apenas o erro404
    # single_contact = Contact.objects.get(pk=contact_id)
    # if single_contact is None:
    #     raise Http404

    # O django tem um atalho para o  código acima
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True) # Também é possível fazer um filter
    contact_name = f'{single_contact.first_name} - '

    context = {
        'contact': single_contact,
        'site_title': contact_name
    }

    return render(
        request,
        'contact/contact.html',
        context
    )