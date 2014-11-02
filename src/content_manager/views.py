from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, Http404
from .models import Description

# Create your views here.
def home(request):
    return render_to_response("home2.html", locals(), context_instance = RequestContext(request))
    
def about(request):
    descriptions = Description.objects.all()
    context = {'descriptions': descriptions}
    template = 'about.html'
    return render(request, template, context)

def art(request):
    justDescriptions = Description.objects.exclude(title = "about")
    descriptions = justDescriptions.order_by('rank')
    if (descriptions.count() == 0):
        slug = "descriptions-needed"
        context = {'slug': slug}
        template = 'art.html'
        return render(request, template, context)
    else:
        try:
            firstDescription = descriptions[0]
            slug = firstDescription.get_slug()
            context = {'descriptions': descriptions, 'slug': slug}
            template = 'art.html'	
            return render(request, template, context)
        except:
            raise Http404

def memoir(request, slug):
    justDescriptions = Description.objects.exclude(title = "about")
    descriptions = justDescriptions.order_by('rank')
    if(descriptions.count() == 0):
        count = 0
        context = {'descptionCount': count}
        template = 'memoir.html'
        return render(request, template, context)
    else:
        try:
            description = Description.objects.get(slug=slug)
            currentSlug = slug 
            context = {'description': description, 'descriptions': descriptions,
                           'slug': currentSlug }
            template = 'memoir.html'	
            return render(request, template, context)
        except:
            raise Http404


#def single(request, slug):
#	try:
#		print slug
#		product = Product.objects.get(slug=slug)
#		context = {'product': product }
#		template = 'products/single.html'
#		return render(request, template, context)
#	except:
#		raise Http404

# Create your views here.
