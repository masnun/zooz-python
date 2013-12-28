# ZOOZ Python Client

#### A Python library for making ZooZ API Calls


## Official Documentation
<br/>

The official docs for ZOOZ can be found on their developer portal - <a href="http://www.zooz.com/developers">http://www.zooz.com/developers</a>. This is an unofficial client library written out of necessity. 

<br/> 
 


## Usages

Import the client:

```
from zooz import ZoozClient
```

Create a new instance of the Client

```
zooz = ZoozClient(unique_id='<unique_id>',
                  app_key='<app_key>',
                  sandbox=True)

```

You can use arguments unpacking with the make_request() method:

```
transaction = {'cmd': 'openTrx',
               'amount': '0.99',
               'currencyCode': 'USD'}

print zooz.make_request(**transaction)

```

Which is equivalent to:

```
print zooz.make_request(cmd='openTrx',amount=0.99, currencyCode='USD')

```

Or you can also directly call the ZooZ commands:

```
print zooz.openTrx(amount=0.99, currencyCode='USD')

``` 