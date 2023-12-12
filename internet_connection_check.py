import requests, time
#from requests.exceptions import ConnectionError

import os

def internet_connection_test(url:str):
  print(f'Attempting to connect to {url} to determine internet connection status.')
  
  # ping uses ICMP protocol
  # pinging with 5 packets via -c flag with 10 second timeout
  response = os.popen(f"ping -c 5 -t 10 {url}")
    
  for line in response.readlines():
      print(line)

  # uses HTTP protocol
	# try:
	# 	print(url)
	# 	resp = requests.get(url, timeout = 10)
	# 	resp.text
	# 	resp.status_code
	# 	print(f'Connection to {url} was successful.')
	# 	return True
	# except ConnectionError as e:
	# 	requests.ConnectionError
	# 	print(f'Failed to connect to {url}.')
	# 	return False
	# except:
	# 	print(f'Failed with unparsed reason.')
	# 	return False
 
def bytes_to_mb(bytes:float):
  # 1e+6
  return float(bytes / pow(1024, 2))

def check_download_speed(url:str):
  print(f'Downloading file from {url} to determine download speed.')
  start_time = time.time()
  response = requests.get(url, stream=True)
  
  # in Bytes
  total_length = float(response.headers.get('content-length'))

  if total_length is not None:
    # time since epoch in seconds
    elapsed_time = time.time() - start_time
    
    print(f'Elapsed time: {elapsed_time}')
    download_speed_mbps = bytes_to_mb(total_length) / elapsed_time
    
    print(f'Total length in mb: {round(bytes_to_mb(total_length), 1)}')
    print(f'Download speed in mbps: {round(download_speed_mbps, 1)}')

internet_connection_test(url='google.com')
check_download_speed(url='https://drive.google.com/uc?export=download&id=1B6rLZwZx9QkzulhB0Pcgci4BXPlHEu3Z')

