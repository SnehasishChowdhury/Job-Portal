from django.shortcuts import render, redirect
from .models import Conversion
from openpyxl import Workbook
import csv
import openpyxl
from openpyxl.utils import get_column_letter
from django.shortcuts import render, redirect
from .models import Conversion

def convert_csv_to_excel(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        conversion = Conversion.objects.create(csv_file=csv_file)

        # Read CSV file
        csv_data = csv.reader(csv_file.read().decode('utf-8'))

        # Create a new workbook
        wb = openpyxl.Workbook()

        # Select the active sheet
        sheet = wb.active

        # Write CSV data to Excel sheet
        for row_data in csv_data:
            sheet.append(row_data)

        # Save the converted Excel file
        excel_file_path = f'media/{conversion.csv_file.name}.xlsx'
        wb.save(excel_file_path)

        # Update the conversion object with the Excel file path
        conversion.excel_file = excel_file_path
        conversion.save()

        return redirect('conversion_list')

    return render(request, 'converter/convert.html')

def conversion_list(request):
    conversions = Conversion.objects.all()
    return render(request, 'converter/conversion_list.html', {'conversions': conversions})