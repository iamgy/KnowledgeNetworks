from web_of_science import WokmwsSoapClient

soap = WokmwsSoapClient()
results = soap.search('nulear energy')

print results