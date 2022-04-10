from django.db.models import fields
from django.shortcuts import redirect, render
from django.views import View
from .forms import BikeForm
from .models import Bike


# Create your views here.


class NewBikeReg(View):

    def get(self, request):
        form = BikeForm()
        return render(request, 'testapp/index.html', {'form':form})
    

    def post(self, request):
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bikeview")
        return render(request, 'testapp/index.html', {'form':form})


class BikeView(View):
    
    def get(self, request):
        bikes = Bike.objects.all()
        return render(request, 'testapp/bikeview.html', {'bikes':bikes})


class BikeUpdate(View):

    def get(self, request):
        bike = Bike.objects.get(pk=int(request.GET["q"])) 
        return render(request,'testapp/bikeupdate.html',{'bike':bike})

    def post(self, request):
        bike = Bike.objects.get(pk=int(request.POST['txtid']))   
        bike.owner_name = request.POST["owner"]
        bike.bike_name =request.POST["bikename"]
        bike.save()
        return redirect('bikeview')


class BikeDelete(View):

    def get(self, request, pk):
        s = Bike.objects.get(id=pk)
        return render(request, "testapp/delete.html",{"bike":s.owner_name})

    def post(self, request, pk):
        s = Bike.objects.get(id = pk)
        if request.method == 'POST':
            s.delete()
            return redirect('/bikeview')
        return render(request, "testapp/delete.html",{"bike":s.owner_name})
            