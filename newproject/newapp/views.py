from django.shortcuts import render
from .forms import QRform
import qrcode as qr
from random import randint

# img=qr.make("https://www.youtube.com/channel/UCY4L5DfiL64smeM0UzoO2kQ")

# img.save("PI-fact_youtube_channel.png")



# Create your views here.
def QR_View(request):
    form=QRform()
    status=False
    qr_code=''
    name=''

    if request.method=='POST':
        form=QRform(request.POST)

        if form.is_valid():
            status=True
            url=form.cleaned_data['url']
            name=form.cleaned_data['name']
            qr_code=(qr.make(url)).save('media/images/'+name+'.png')
            print('img saved')

    return render(request,'newapp/qrcode.html',{'form':form,'status':status,'qr-code':qr_code,'name':name})
    