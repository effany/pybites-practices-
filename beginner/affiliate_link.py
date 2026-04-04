def generate_affiliation_link(url):
    url_parts = url.split("/")
    id = url_parts[5]
    new_url = f"http://www.amazon.com/dp/{id}/?tag=pyb0f-20"
    return new_url
    
    
    

generate_affiliation_link('https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art')
generate_affiliation_link('https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1')
generate_affiliation_link('https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234')
generate_affiliation_link('https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X')
generate_affiliation_link('https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/')