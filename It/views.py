from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')


from .models import Student, Student
def studentlist(request):
    students  = Student.objects.all()
    context  = {'students': students}
    return render(request, 'studentlist.html', context) 


def studentdetail(request, pk):
    student = Student.objects.get(pk=pk)
    context = {'student': student}
    return render(request, 'studentdetail.html', context)

from .forms import StudentForm
def studentreg(request):
    stu = Student.objects.all() 

    form = StudentForm
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlist')  

    context = {'stu': stu, 'form': form}
    return render(request, 'studentreg.html', context) 



def studentupdate(request, id):
	obj = get_object_or_404(Student, id =id)
	form = StudentForm(request.POST or None, instance = obj)
	data = Student.objects.get(id = id)
	if form.is_valid():
		form.save()
		return redirect('studentlist')

	context = {'form':form, 'data':data}
	return render(request,'studentupdate.html', context )


def studentdelete(request, id):
	data = Student.objects.get(id = id)
	context = {'data':data}
	if request.method =='POST':
		data.delete()
		return redirect('form')
	return render(request,'studentdelete.html', context )


from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class StudentReg(CreateView):
	model = Student
	fields = '__all__'
	template_name = 'CBV/studentreg.html'
	success_url ="/"

class Studentlist(ListView):
	model = Student
	template_name = 'CBV/studentlist.html'

class Studentdetail(DetailView):
	model =Student
	template_name = 'CBV/studentdetail.html'

class StudentUpdate(UpdateView):
	model = Student
	fields = "__all__"
	template_name = 'CBV/studentupdate.html'
	success_url ="/"


class StudentDelete(DeleteView):
	model = Student
	template_name = 'CBV/studentdelete.html'
	success_url ="/"



