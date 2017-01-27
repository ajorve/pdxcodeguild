"""
Write a function named extract_domain that will print the first matching domain name in a given string.

>>> extract_domain("kieran@pdxcodeguild.com")
pdxcodeguild.com

>>> extract_domain("domain of jwackman@hvc.rr.com designates 2a00:1450:400c:c09::22d as permitted sender")
hvc.rr.com
"""

def extract_domain(url):
    at_index = url.find('@')
    dotcom_index = url.find('.com')
    return(at_index, dotcom_index+4)

## string.split("@")[1].rstrip(".com")
## fromAddr = message.get('From').split('@')[1].rstrip('>')
        ## fromAddr = fromAddr.split(' ')[0]
# extract_domain(header_info)
