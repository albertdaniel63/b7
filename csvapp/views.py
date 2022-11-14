from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from csvapp.models import Csv_emp
import csv
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, template_name='home.html')


def export_csv(request):
    all_active = Csv_emp.objects.filter(active = True)
    response = HttpResponse(content_type = 'csv/txt')
    csv_writer = csv.writer(response)
    csv_writer.writerow(["ID", "Name", "Salary", "Company",
                        "Designation", "DOJ", "Active"])
    

    for emp in all_active.values_list('id','name','company','salary','designation','DOJ','active'):
        csv_writer.writerow(emp)
    
    response['Content-Disposition'] = 'attachment; filename = "employee-data.csv"'
    return response

def upload_csv(request):
    data ={}
    if "GET" == request.method:
        return render(request,'upload.html',data)
    try:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponseRedirect(reverse("upload_csv"))

        if csv_file.multiple_chunks():
            return HttpResponseRedirect(reverse("upload_csv"))

        file_data = csv_file.read().decode('utf-8')

    except Exception as e:
        print(e)

    return HttpResponseRedirect(reverse("upload_csv"))


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('csvapp:success')

    def form_valid(self,form):
        form.send()
        return super().form_valid(form)

# function based view
# if request.method == 'POST':
#     form = ContactForm(request.POST)
#     if form.is_valid():
#         form.send()
#         return redirect('contact:success')
# else:
#     form = ContactForm())

class ContactSuccessView(TemplateView):
    template_name = 'success.html'


























# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         upl_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(upl_file.name,upl_file)
#         print(name,fs.url(name))
#         context['url'] = fs.url(name)
#     return render(request,'upload.html',context)

# def all_books(request):
#     books = Csv_book.objects.all()
#     return render(request,'all_books.html',{'all_books':books})



