from urllib.request import urlopen

def download(url):
    # This script can get the response and save data into file
    try:
        data = urlopen(t_url).read()
    except (http.client.IncompleteRead) as e:
        data = e.partial

    txt_str = str(data)
    lines = txt_str.split("\\n")

    # Destination file name
    des_url = 'test.txt'
    
    # Create a new file
    fx = open(des_url,"w")

    # Write response lines one by one into text file
    for line in lines:
        fx.write(line+ "\n")
    fx.close()

#url = 'https://static.turi.com/datasets/millionsong/10000.txt'

#download(url)

