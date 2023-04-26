import requests
def UrlData():
    for i in range(1,5):
        print(i)
        url = f"https://demo.credy.in/api/v1/maya/movies/?page={i}"
        print(url,'--------------------------------------------------------------')
        response = requests.get(url)
        data = response.json()
        movies = data['results']
        return movies

