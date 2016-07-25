'''
Dwolla makes it easy to send money to anyone who's connected to the internet. In this example know Dwolla by sending money 
to your email address. 
'''

email = 'tulswani19@gmail.com' # Your email ID

# Dwolla REST Client
from dwolla import DwollaUser

Dwolla = DwollaUser('OAUTH_TOKEN')

transaction = Dwolla.send_funds(0.01, email, 'PIN', dest_type='Email')

print('Transaction ID: %s' % transaction)
