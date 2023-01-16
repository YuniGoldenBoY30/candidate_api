# import os
# from django.conf import settings
# from django.http import HttpResponse
# from django.template.loader import get_template
# from rest_framework import status
# from rest_framework.response import Response
# from xhtml2pdf import pisa
# from django.http import HttpResponse
# from django.template.loader import render_to_string
#
# from weasyprint import HTML


class Export:
    pass
    # @staticmethod
    # def link_callback(uri, rel):
    #     sUrl = settings.STATIC_URL  # Typically /static/
    #     sRoot = settings.STATIC_ROOT  # Typically os.path.join(BASE_DIR, 'static')
    #     mUrl = settings.MEDIA_URL  # Typically /media/
    #     mRoot = settings.MEDIA_ROOT  # Typically os.path.join(BASE_DIR, 'media')
    #     if uri.startswith(mUrl):
    #         path = os.path.join(mRoot, uri.replace(mUrl, ""))
    #     elif uri.startswith(sUrl):
    #         path = os.path.join(sRoot, uri.replace(sUrl, ""))
    #     else:
    #         return uri
    #     if not os.path.isfile(path):
    #         raise Exception(
    #             'media URI must start with %s or %s' % (sUrl, mUrl)
    #         )
    #     return path
    #
    # @staticmethod
    # def export_pdf(list_record):
    #     data = {"data": list_record}
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #
    #     template = get_template('template_pdf.html')
    #     html = template.render(data)
    #     pisa_status = pisa.CreatePDF(
    #         html, dest=response, link_callback=Export.link_callback)
    #     if pisa_status.err:
    #         return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisa_status.err, html))
    #     return response

    # @staticmethod
    # def export_pdf_(records):
    #     html = render_to_string("template_pdf.html", records)
    #
    #     response = HttpResponse(content_type="application/pdf")
    #     response["Content-Disposition"] = "inline; report.pdf"
    #
    #     HTML(string=html).write_pdf(response)
    #
    #     return response
