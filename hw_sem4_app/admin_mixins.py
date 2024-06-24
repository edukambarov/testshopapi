import csv
import datetime

from django.db.models.options import Options
from django.http import HttpResponse

from .models import Good


class ExportAsCSVMixin:
    def export_as_csv(self, request, queryset):
        meta: Options = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv; charset=windows-1251')
        response['Content-Disposition'] = 'attachment; filename={}-export.csv'.format(meta)
        fields_ = [field for field in meta.get_fields()]
        result = csv.writer(response, delimiter=";")
        result.writerow(field_names)
        for obj in queryset:
            result.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = 'Export as CSV'


    def export_manytomany_as_csv(self, request, queryset):
        meta: Options = self.model._meta
        response = HttpResponse(content_type='text/csv; charset=windows-1251')
        response['Content-Disposition'] = 'attachment; filename={}-export.csv'.format(meta)
        result = csv.writer(response, delimiter=";")
        fields = [field for field in meta.get_fields()]
        result.writerow([field.name.title() for field in fields])
        for obj in queryset:
            data_row = []
            for field in fields:
                if field.many_to_many == True:
                    try:
                        values = list(getattr(obj, field.name).all().values_list('id',flat=True))
                    except:
                        value = str(obj).replace(";","")
                else:
                    value = str(getattr(obj, field.name)).replace(";","")
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y')
                data_row.append(value)

            if values != None:
                for data in values:
                    try:
                        good = Good.objects.get(pk=data)
                        data_row[-1] = str(good)
                    except:
                        data_row[-1] = data
                    result.writerow(data_row)
            else:
                result.writerow(data_row)
        return response

    export_manytomany_as_csv.short_description = 'Export many-to-many data as CSV'

