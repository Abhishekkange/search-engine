
from Flask import jsonify

@app.get('/search/<query>')
def search(query):
    result = search_mod(query).jsonify()
    return result
