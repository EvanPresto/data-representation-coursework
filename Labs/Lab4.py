import pip._vendor.requests as requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
    response = requests.get(url)
    return response.json()

def getBookByID(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):
    book = {'Author': 'test test test',
            'Price': 123412,
            'Title': 'testing title',
            'id':265
            }
    response = requests.post(url, json = book)
    return response.json()

def updateBook(id,bookdif):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl , json=bookdif)
    return response.json()

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if  __name__ == "__main__":
    #print(getallbooks())
     #print(getBookByID(363))
     #print(createBook({}))
     bookdif = { "Price":10000 }
     print(updateBook(363,bookdif))
   
