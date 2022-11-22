from django.shortcuts import render
from .forms import FileForm
from businesses.models import Business
from businesses.serializers import BusinessSerializer
from transactions.models import Transaction
from utils.transaction_type_finder import transaction_type_finder
from businesses.errors.my_errors import LengthError, FileTypeError
import ipdb

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['file'].name
            if filename[-4:] != ".txt":
                raise FileTypeError('Ensure given file is a .txt file.')

            file = request.FILES['file']
            lines = [ line.decode('utf-8') for line in file.readlines() ]
            
            line_check = lines[0]
            if len(lines) == 1 :
                line_limit = 80
            else:
                line_limit = 82
            if len(line_check) != line_limit:
                raise LengthError('Ensure each line has the correct amount of characters.')

            for line in lines:
                owner_name = line[48:62]
                business_name = line[62:80]
                business, _ = Business.objects.get_or_create(owner_name=owner_name, business_name=business_name)
                
                transaction_type = line[0]
                transaction = transaction_type_finder(transaction_type)
                
                value_string = line[9:19]
                value = int(value_string) / 100

                transaction['value'] = value
                Transaction.objects.create(**transaction, business=business)

    else: 
        form = FileForm()

    businesses = Business.objects.all().order_by('business_name')
    serializer = BusinessSerializer(businesses, many=True)
    index = 0
    for business in serializer.data:
        business.transactions = businesses[index].transactions.all()
        index += 1

    return render(request, 'businesses/index.html', {'form': form, 'businesses': serializer.data})
    