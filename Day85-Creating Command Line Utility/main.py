#command line utility means commands to do something, simply which is used for some tasks like curl command in cmd is used to download files

#in python we can create commands like curls

#In Python, you can create your own command line utilities using the built-in argparse module.

import argparse
import requests
def download_file(url, local_filename): 
  if local_filename is None:
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
  with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192): 
              # If you have chunk encoded response uncomment if
              # and set chunk_size parameter to None.
              #if chunk: 
              f.write(chunk)
  return local_filename
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save yout file")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)
# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url,args.output)

#Note to run the file instead of python terminal choose cmd from + button and then type:
# python main.py https://imagej.net/images/AuPbSn40.jpg -o nischal.jpg
# nischal.jpg will be file name 
# https:// will be link
# if not provided name then this program will not be proceed 