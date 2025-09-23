from tracker import travel_records


travel_records('kerala','25/07/2025','god\'s own country')
travel_records('delhi','20/07/2025','India\'s capital territory')
travel_records('talilnadu','15/07/2025','The tenth largest Indian state by area and the sixth largest by population')




# import code:
# -----------------

# import json
# def travel_records(name,date,comment):
#     dateval=date
#     date_obj=datetime.strptime(dateval,"%d/%m/%Y")
#     format_dt=date_obj.strftime("%d %B,%Y")


#     details={
#         "CityName":name,
#         "visitedDate":format_dt,
#         "comment":comment
#     } 
#     m=details
#     for x,y in m.items():
#         print(x,y)