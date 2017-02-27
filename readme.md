# Flask PDF - render any page in PDF

Great for a best printing result or an easy downloadable version
of a Flask web page.

## Requirements

- a Flask project with Python 3
- [wkhtmltopdf](http://wkhtmltopdf.org/) installed on the server


## Installation

    pip install -e git+https://github.com/vinyll/flask-pdf.git#egg=flaskpdf

In your flask file, add:

    from flask import Flask
    import flaskpdf

    app = Flask(__name__)
    flaskpdf.init_app(app)

Now browse any of your webpage adding '_.pdf_' extensions.
eg: http://example.org/page/1 is downloadable at http://example.org/page/1.pdf.

You could easily make a printer-friendly version of your current page:

    <a href="{{ request.path }}.pdf">Print this page</a>


## Configuration

You may want to tune the default configuration.
To do so, [read the Flask config documentation](http://flask.pocoo.org/docs/0.12/config/),
and play with these settings:

    # The URL to access a webpage download in PDF format
    PDF_URL_RULE = '/<path:path>.pdf'

    # The path and options for wkhtmltopdf executation.
    # `{url}` will be replaced by the url of the page to transform
    # and `{output}` will be a temporary output file (auto-deleted).
    PDF_WKHTMLTOPDF_COMMAND = 'wkhtmltopdf --print-media-type {url} {output}'
