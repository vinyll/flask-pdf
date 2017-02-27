from subprocess import check_output, call
from tempfile import NamedTemporaryFile

from flask import request, Response


def init_app(app):
    @app.route(app.config.get('PDF_URL_RULE', '/<path:path>.pdf'),
               methods=['get'])
    def download_pdf(path):
        tmp_file = NamedTemporaryFile()
        command = app.config.get('PDF_WKHTMLTOPDF_COMMAND', 'wkhtmltopdf '
                                 '--print-media-type {url} {output}')
        check_output(command.format(url='{}{}'.format(request.url_root, path),
                                    output=tmp_file.name),
                     shell=True)
        response = Response(tmp_file.file.readlines())
        response.mimetype = 'application/pdf'
        response.headers['Content-Disposition'] = (
            'attachment; filename={}.pdf'.format(path.replace('/', '_')))
        tmp_file.close()
        return response

version = '0.1'
