from zooz import ZoozClient

zooz = ZoozClient(unique_id='aircourts.web',
                  app_key='8c037c03-9717-4922-861d-9ca278e61380',
                  sandbox=True)

transaction = {'cmd': 'openTrx',
               'amount': '0.99',
               'currencyCode': 'USD'}

print zooz.make_request(**transaction)

print zooz.openTrx(amount=0.99, currencyCode='USD')
