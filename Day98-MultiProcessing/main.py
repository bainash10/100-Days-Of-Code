#Threads are lightweight, and are inside processes
import multiprocessing
import requests

def downloadFile(url,name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"Day98-MultiProcessing/files2/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    pros=[]
    for i in range(5):
        #downloadFile(url,i) -> not parallely downloaded
        #To download file parallely:
        p= multiprocessing.Process(target=downloadFile, args=(url,i))
        p.start()
        pros.append(p)  #process are appended in list pros

    for p in pros:
        p.join()
