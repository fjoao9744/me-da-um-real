from django.shortcuts import render
from pypix.pix import Pix

def view(request):
    pix = Pix()

    pix.set_name_receiver('João Programador')
    pix.set_city_receiver('COLATINA')
    pix.set_key('8fffcc1a-cd0f-4f92-8af1-266e1fa13f43')
    pix.set_amount(1.0)
    pix.set_description('Você faria isso por mim? 🤗')
    pix.set_identification('TX123')
    
    return render(request, 'index.html', {"pix": pix.get_br_code(), "image": pix.save_qrcode()})
