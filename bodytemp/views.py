from django.shortcuts import redirect, render

from .models import BTemp
from .forms import BTForm

def index(request):
	data = BTemp.objects.all().order_by('edate').reverse()
	params = {
		'title': 'その日の体温',
		'data': data,
		'form': BTForm(),
	}
	if (request.method=='POST'):
		edate = request.POST['edate']
		btemp = request.POST['btemp']
		#if same date find, overwrite data
		fdate = BTemp.objects.filter(edate=edate)
		if fdate.count() > 0:
			#edit
			obj = BTemp.objects.get(edate=edate)
			btmp = BTForm(request.POST, instance=obj)
		else:
			btmp = BTemp(edate=edate,btemp=btemp)
		btmp.save()
		return redirect(to='/bodytemp')
	return render(request, 'bodytemp/index.html', params)

def delete(request, dt):
	btemp = BTemp.objects.get(edate=dt)
	if (request.method=='POST'):
		btemp.delete()
		return redirect(to='/bodytemp')
	params = {
		'title': 'その日の削除',
		'data': btemp,
	}
	return render(request, 'bodytemp/delete.html', params)