from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PKSerializer
from .models import PK, Purchase
from django.views.generic.edit import CreateView

def index(request):
    products = PK.objects.order_by('-id')
    context = {'products': products}
    return render(request, 'myapi/index.html', context)

class PKViewSet(viewsets.ModelViewSet):
    queryset = PK.objects.all().order_by('name')
    serializer_class = PKSerializer

class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f' <h3 style="text-align: center; margin-top: 300px">'
                            f'Спасибо за покупку, {self.object.person}, '
                            f'в ближайшее время по указаному вами номеру '
                            f'телефона с вами свяжется наш менеджер, '
                            f'для согласования деталей заказа  !</h3>')