from tripdata import trip_details


trip_details('kerala',"01/06/2020",'god\'s own country')

trip_details('delhi','15/09/2025','India\'s capital territory')

trip_details('tamilnadu','20/09/2025','The tenth largest Indian state by area and the sixth largest by population')

trip_details('Karnataka','24/08/2025','Karnataka, the 7th largest state in terms of area in India')

trip_details('Assam','24/09/2025','Assam is special for its diverse culture, including vibrant festivals and the Bihu festival')










# module creation code
# ----------------------

# from datetime import datetime
# import json

# def trip_details(city,visiteddate,comment):
#     date_str=visiteddate
#     date_object=datetime.strptime(date_str,"%d/%m/%Y")
#     formated_dt=date_object.strftime("%B %d, %Y")
#     trip={
#         "CityName":city,
#         "VisitedDate":formated_dt,
#         "Comment":comment

#     }
#     conv_json=json.dumps(trip)
#     print(conv_json)