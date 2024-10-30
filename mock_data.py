
def mock_list():
    return [
        {
            "id": 1,
            "name": "Top 10 des meilleurs albums de tous les temps",
            "description": "Une liste des 10 meilleurs albums de tous les temps",
            "is_private": False
        },
        {
            "id": 2,
            "name": "Top 10 des meilleurs albums de Daft Punk",
            "description": "Une liste des 10 meilleurs albums de Daft Punk",
            "is_private": False
        },
        {
            "id": 3,
            "name": "Top 10 des meilleurs albums de Justice",
            "description": "Une liste des 10 meilleurs albums de Justice",
            "is_private": False
        }
    ]
    
def mock_list_release():
    return [
        {
            "id_list": 1,
            "rank": 1,
            "release": 1,
        },
        {
            "id_list": 1,
            "rank": 2,
            "release": 2,
        },
        {
            "id_list": 2,
            "rank": 1,
            "release": 2,
        },
    ]

def mock_fetch_artists():
    return [
        {
            "name": "Daft Punk",
            "id": 1
        },
        {
            "name": "Justice",
            "id": 2
        },
        {
            "name": "Kavinsky",
            "id": 3
        }
    ]

def mock_fetch_releases():
    return [
        {
            "title": "Discovery",
            "date": "2001-03-12",
            "artist": 1
        },
        {
            "title": "Cross",
            "date": "2007-06-11",
            "artist": 2
        },
        {
            "title": "OutRun",
            "date": "2013-02-25",
            "artist": 3
        }
    ]