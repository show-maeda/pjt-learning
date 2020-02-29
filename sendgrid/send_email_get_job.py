import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = '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'


def main(office_id=1,
         office_name='施設名',
         owner_name='法人名',
         employment_type='雇用形態',
         address='住所',
         memo='メモ',
         row=1):
    from_email = 's.maeda.fukui@gmail.com'
    to_email = 's.maeda.fukui@gmail.com'
    subject = '【法人問い合わせ】'+ owner_name + ' ' + office_name + ' / (求人)' + employment_type
    body_l = ['きらケア CSサポートグループ 様',
              '',
              '企業問い合わせがありましたのでご報告させて頂きます。',
              '下記が問い合わせ情報になります。',
              '',
              '【企業名】',
              owner_name,
              office_name,
              '',
              '【住所】',
              address,
              '',
              '【問い合わせ内容(求人募集)】',
              '• 雇用形態',
              employment_type,
              '',
              '• 自由記述',
              memo,
              '',
              '【シートURL】',
              'https://docs.google.com/spreadsheets/d/18PI57-3zLBC_e9Un9OPfnQPkG2Jd2OFtHw2e_DdqJQw/edit#gid=2042022389&range=' + str(row) + ':' + str(row),
              '',
              '【DF URL】',
              'https://df.lvgs.jp/office/' + str(office_id) + '/show/',]
    body = '\n'.join(body_l)

    data = {
            "personalizations": [{
                "to": [{
                    "email": to_email}],
                "subject": subject}],
            "from": {"email": from_email},
            "content": [{"type": "text/plain",
                           "value": body}],
            "tracking_settings": {
                "click_tracking": {
                    "enable": False,
                    "enable_text": False},
                }
        }

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()