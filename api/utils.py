import io
import csv
import logging

from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

logger = logging.getLogger('__name__')

def send_test_csv_report(test_results, recipients):
    filename = 'test_csv_report.csv'
    string = io.StringIO()
    csv_writer = csv.writer(
        string,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )

    csv_writer.writerow([
        'S.No',
        'Test Name',
        'Test Result',
        'Test Description',
    ])

    for resutl_index, result in enumerate(test_results):
        csv_writer.writerow([
            resutl_index + 1,
            result['test_name'],
            result['result'],
            result['test_description']
        ])

    email = EmailMultiAlternatives(
        subject = str(timezone.now().strftime("%d-%m-%Y")) + " " + 'Test Results' + 'csv report',
        from_email='omarehap177@gmail.com',
        to = recipients
    )
    email.attach(
        filename=filename,
        mimetype = "text/csv",
        content=string.getvalue()
    )
    email.send()
    logger.info('Email Sent Successfully')