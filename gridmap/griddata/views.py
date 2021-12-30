from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import GridNode, GridArea, GridSupport, GridMember
from .forms import GridMemberForm, GridSupportForm
from maphandle import map



# Create your views here.
def index(request):

    rs = GridNode.objects.all()

    figure = map.show_all_grid(rs)

    gns = [{"id":str(gn.id),"name":gn.name} for gn in rs]
    context = {'gridnodes': gns, 'map':figure}
    return render(request, 'index.html', context)

def gridnode(request, gnid):
    gn = GridNode.objects.get(pk=gnid)
    figure = map.show_area_json(str(gn.gridarea))
    context = {'gridnode':gn, 
    'members':gn.gridmembers, 
    'support':gn.gridsupport,
    'area':gn.gridarea,
    'map':figure}
    return render(request, 'gridnode.html', context)
    
def edit_support(request, gnid):
 
    gn = GridNode.objects.get(pk=gnid)
    if(request.method == 'POST'):
        f = GridSupportForm(request.POST, instance=gn.gridsupport)
        f.save()
        return HttpResponseRedirect('/gn/'+str(gnid))

    f = GridSupportForm(instance=gn.gridsupport)

    context = {'gridnode':gn, 
    'support':gn.gridsupport,
    'form':f
    }
    return render(request, 'esupport.html', context)

def edit_member(request,gnid):
    gn = GridNode.objects.get(pk=gnid)
    if(request.method == 'POST'):
        f = GridMemberForm(request.POST)
        newform = f.save()

        return HttpResponseRedirect('/emembers/'+str(gnid))
    mmodel = GridMember()
    mmodel.gridnode = gn
    newform = GridMemberForm(instance=mmodel)
    context = {'gridnode':gn, 
    'members':gn.gridmembers, 
    'support':gn.gridsupport,
    'form': newform}

    return render(request, 'emembers.html', context)

def del_member(request):
    
    if(request.method == 'POST'):
        memberid=int(request.POST.get('memberid'))
        obj = GridMember.objects.get(pk=memberid)
        gnid = obj.gridnode.id
        obj.delete()
        return HttpResponseRedirect('/emembers/'+str(gnid))

    else:
        return HttpResponseRedirect('/')

    