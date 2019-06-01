from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.db import connections
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
import csv
from .models import Product
from django.conf import settings
import psycopg2
import os


# Create your views here.
class FileUploadView(View):
    form_class = FileUploadForm
    template_name = 'core/file_upload.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request, *args, **kwargs):
        try:
            fs = FileSystemStorage(file_permissions_mode=0o755)
            file_name = fs.save(str(request.FILES['file'].name), request.FILES['file'])
            csv_file_path = os.path.abspath(file_name)
            conn = connections['default']
            cur = conn.cursor()
            db_table = Product._meta.db_table
            cur.execute("BEGIN")
            cur.execute("COPY" +
                        " {}(name,sku,description)".format(Product._meta.db_table) +
                        "FROM '" + csv_file_path + "' WITH DELIMITER ',' CSV HEADER ;")
            cur.execute("DELETE FROM"
                        " {0} a USING {0} b".format(db_table) +
                        " WHERE a.id < b.id AND lower(a.sku) = lower(b.sku);")
            cur.execute("UPDATE {} SET active = random() > 0.5 WHERE  active IS NULL;".format(db_table))
            cur.execute("COMMIT")
        except Exception as e:
            raise (e)
        finally:
            if os.path.exists(csv_file_path):
                os.remove(csv_file_path)
        return HttpResponse("Uploaded")
