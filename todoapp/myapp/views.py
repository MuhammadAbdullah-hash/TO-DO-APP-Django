from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import Items_data
from . forms import Items_data_Form



def main_app(request):
	if request.method == 'GET':
		data = list(Items_data.objects.all())
		id_list= list( range(len(data)) )
		data_2 = list(zip( data , id_list ))
		return render(request, 'myapp/basic.html' , { 'data_all' : data_2 , 'message': 'none' } )
	elif request.method == 'POST' : 
		item_name = request.POST.get( 'element_name' , 'None' )
		if item_name != 'None':
			text = 'Already added'
			if Items_data.objects.filter(name = item_name).count() == 0 : 
				new_item = Items_data( name = item_name )
				new_item.save()
				text = 'none'
			data = Items_data.objects.all()
			id_list= list( range(len(data)) )
			data_2 = list(zip( data , id_list ))		
			return render(request, 'myapp/basic.html' , {'data_all' : data_2 ,  'message' : text } )
		else :
			data = Items_data.objects.all()
			id_list= list( range(len(data) ) )
			data_2 = list(zip( data , id_list ))
			text = ''
			return render(request, 'myapp/basic.html' , {'data_all' : data_2 ,  'message' : text } )


def delete_item(request) :
	name = request.POST.get('element_name' , 'None')
	Items_data.objects.filter(name = name).delete()	
	return redirect('/')


def edit_item(request) :
	name = request.POST.get('element_name' , 'None')
	status = request.POST.get('element_status' , 'None')
	if request.method == 'POST':
		return render(request, 'myapp/edit.html' , {'name' : name , 'val' : status}  )
	elif request.method == 'GET' :
		new_name = request.GET.get( 'new_name' , 'None')
		new_status = request.GET.get( 'new_status' , 'None' )
		org_name = request.GET.get('org_name' , 'None')
		org_status = request.GET.get('org_status' , 'None')
		if (new_status != org_status) or (new_name != org_name):
			obj = Items_data.objects.get(name = org_name)
			obj.name = new_name
			if new_status == 'Done' :
				obj.is_done = True
			elif new_status == 'Pending' :
				obj.is_done = False
			obj.save()
		return redirect('/')

