from django.shortcuts import render
from agentapp.models import agent,location,contact_info,address
from django.http import HttpResponse
def home(request):
    return render(request,'agent.html')
def agentform(request):
    return render(request,'agent_form.html')
def contactform(request):
    return render(request,'contact_form.html')
def locationform(request):
    return render(request, 'location_form.html')
def addressform(request):
    return render(request, 'address_form.html')
def agentinsert(request):
    try:
        Agentid=request.GET['agentid']
        First_name=request.GET['firstname']
        Lastname=request.GET['lastname']
        Experience=request.GET['experience']
        Company_name=request.GET['company']
        p1=agent(agentid=Agentid,firstname=First_name,lastname=Lastname,experience=Experience,company=Company_name)
        p1.save()
        return HttpResponse("<h1>agent data inserted succefully </h1>")
    except Exception as a:
        return HttpResponse(a)
def contactinsert(request):
    try:
        Contact_id=request.GET['contactid']
        agent1=str(request.GET['agentid'])
        Agentid=agent.objects.get(agentid=agent1)
        mobile_no=request.GET['mobileno']
        Email=request.GET['email']
        contact_info(contactid=Contact_id,agentid=Agentid,mobileno=mobile_no,email=Email).save()
        return HttpResponse("<h1> contacts data inserted succefully </h1>")
    except Exception as e:
        return HttpResponse(e)

def locationinsert(request):
            try:
                LOCATION_ID = request.GET['locationid']
                Agent2 = str(request.GET['agentloc'])
                AGENT = agent.objects.get(agentid=Agent2)
                LOC_NAME = request.GET['locname']
                LOC_CITY = request.GET['loccity']
                LOC_STATE = request.GET['locstate']
                PINCODE = int(request.GET['pincode'])
                l1 = location(locationid=LOCATION_ID, agentloc=AGENT, locname=LOC_NAME, loccity=LOC_CITY,
                              locstate=LOC_STATE, pincode=PINCODE)
                l1.save()
                return HttpResponse("<h1> location data inserted succefully </h1>")
            except Exception as e:
                return HttpResponse(e)
def addressinsert(request):
    try:
        Addressid = request.GET['addressid']
        Agent3 = str(request.GET['agentid'])
        Agentid = agent.objects.get(agentid=Agent3)
        Addressline1 = request.GET['addressline1']
        Addressline2 = request.GET['addressline2']
        City = request.GET['city']
        State = request.GET['state']
        Pincode = request.GET['pincode']
        Landmark = request.GET['landmark']
        a1 = address(addressid=Addressid, agentid=Agentid, addressline1=Addressline1, addressline2=Addressline2,
                     city=City, state=State, pincode=Pincode, landmark=Landmark)
        a1.save()
        return HttpResponse("<h1> Address data inserted succefully </h1>")
    except Exception as ad:
        return HttpResponse(ad)
def agents(request):
    agentrecords=agent.objects.all()
    return render(request,'agents_display.html',{'agentrecord':agentrecords})
def contacts(request):
    agentrecords1=contact_info.objects.all()
    return render(request,'contacts_display.html',{'agentrecord1':agentrecords1})
def locations(request):
    agentrecords2=location.objects.all()
    return render(request,'locations_display.html',{'agentrecord2':agentrecords2})
def addresses(request):
    agentrecords3=address.objects.all()
    return render(request,'addresses_display.html',{'agentrecord3':agentrecords3})
def infoinput(request):
    return render(request,'infoinput.html')
def infodisplay(request):
    agent_id=request.GET['agentid']
    op_type=request.GET['operation']
    if op_type=="agentinfo":
        a = agent.objects.filter(agentid=agent_id)
        return render(request, 'agent_details.html', {'records': a})
    elif op_type=="contactinfo":
        c = contact_info.objects.filter(agentid=agent.objects.get(agentid=agent_id))
        return render(request, 'contact_details.html', {'records2': c})
    elif op_type=="locationinfo":
        l = location.objects.filter(agentloc=agent.objects.get(agentid=agent_id))
        return render(request, 'location_details.html', {'records3': l})
    else:
        ad = address.objects.filter(agentid=agent.objects.get(agentid=agent_id))
        return render(request, 'address_details.html', {'records4': ad})








