import requests



def get_dist_dur(start, end):

    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {

        "origins": start,

        "destinations": end,

        "key": "Enter API Key here"

    }



    response = requests.get(base_url, params=params)



    if response.status_code == 200:

        data = response.json()

        if data["status"] == "OK":

            distance = data["rows"][0]["elements"][0]["distance"]["text"]

            duration = data["rows"][0]["elements"][0]["duration"]["text"]

            return distance

        else:

            print("Request failed.")

            return None, None

    else:

        print("Failed to make the request.")

        return None, None


# distance, duration = get_dist_dur(start, end)

# if distance and duration:

#     pdistance = (f"Driving Distance: {distance}")

#     pduration = (f"Driving Duration: {duration}")
    
    




    
    
