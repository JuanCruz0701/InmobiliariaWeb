from django.shortcuts import render,get_object_or_404,redirect
from .forms import PropertyForm,PropertyBuyForm
from .models import Property,PropertyBuy


# Create your views here.


def PropertyView(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)

       

        if form.is_valid():
            form.save()
        properties = Property.objects.all()
        context = {
            "properties": properties,
            "form": form
        }
        return render(request,"properties/property_list.html", context=context)
    else:
        form = PropertyForm()
        context = {
            "form": form
        }
        return render(request, "properties/property_form.html",context=context)
    
def PropertyDetailView(request, property_id):
    # Recupera la propiedad con el id dado o devuelve un error 404 si no existe
    property = get_object_or_404(Property, id=property_id)
    form = PropertyBuyForm()
    context = {
        "property": property,
        "form": form,
    }

    return render(request, "properties/property_info.html", context=context)

def buy_property(request, property_id):

    property = get_object_or_404(Property, id=property_id)
   # PropertyBuy.objects.create(buyer=request.user, property=property)
    if request.method == "POST":
        form = PropertyBuyForm(request.POST)
        if form.is_valid():
            property_buy = form.save(commit=False)
            property_buy.buyer = request.user
            property_buy.property = property
            property_buy.save()
            return redirect('property_detail', property_id=property.id)
        else:
            form = PropertyBuyForm()

    return render(request, 'properties/buy_property.html', {'form': form, 'property': property})

def nombre_de_tu_vista(request):
    properties = Property.objects.all()

    colony = request.GET.get('colony')
    if colony:
        properties = properties.filter(colony__icontains=colony)

    city = request.GET.get('city')
    if city:
        properties = properties.filter(city__icontains=city)

    type = request.GET.get('type')
    if type:
        properties = properties.filter(type=type)

    ranking = request.GET.get('ranking')
    if ranking:
        properties = properties.filter(ranking=ranking)

    return render(request, 'base.html', {'properties': properties})
    
    
   
    