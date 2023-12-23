import customtkinter as ctk
import tkinter as tk
import maps  
import csv



ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.title("Distance Calculator")

width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry("1000x800")


# def calculate(): #Main_Button function
#     distance, duration = maps.get_dist_dur(start.get(),end.get()) #Get the API function from maps.py
#     distance_box.delete("0.0", "end") #clear result box
#     distance_box.insert("0.0", distance + '\n') #Enter results into result box
#     distance_box.insert("3.0", duration)

count=0
wp_list=[]
wp_km=[]
location_save_list = []
price_s = []
rate_s = []
   
def add_location(): 
    global count
    count += 1  
     
    
    if count == 1:
        distance = maps.get_dist_dur(start.get(),wp.get())
        dist = (f"{start.get()} to {wp.get()}: {distance}")
        
        wp_list.append(wp.get())
        wp_km.append(float(distance.replace('km', '')))
        
        location_save_list.append(f"{start.get()} to {wp.get()}")
        
        distance_box.insert("0.0", dist + '\n') #Enter results into result box
        
        
    else: 
        distance = maps.get_dist_dur(wp_list[count-2],wp.get()) #Get last item of list to find distance to next location
        dist = (f"{wp_list[count-2]} to {wp.get()}: {distance}")
        
        wp_list.append(wp.get())
        wp_km.append(float(distance.replace('km', '')))
        
        location_save_list.append(f"{wp_list[count-2]} to {wp.get()}")
        
        distance_box.insert(f"{count+1}.0", dist + '\n') #Enter results into result box
             

          
def calculate():
    total_distance_box.delete("0.0", "end")
    total = sum(wp_km)
    total_distance_box.insert("0.0",f"Total Distance: {total} km" + '\n')
    
    rater = rate.get()
    try:
        price = float(rater.replace("LKR", ""))*total
    except ValueError:
        return
    total_distance_box.insert("2.0",f"Total Price: {price} LKR")
    
    rate_s.append(rater)    
    price_s.append(price)
              
    
def clear():
    distance_box.delete("0.0", "end")
    total_distance_box.delete("0.0", "end")
    start.delete("0","end")
    end.delete("0","end")
    wp.delete("0","end")
    rate.delete("0","end")
    
    wp_list.clear()
    wp_km.clear()
    location_save_list.clear()
    price_s.clear()
    rate_s.clear()
    
    
    
def options(choice):
    rate.delete("0","end")
    if choice == "Van":
        rater = 120
        rate.insert("0",f"{rater} LKR")
    else:
        rater = 90
        rate.insert("0",f"{rater} LKR")
        
def save():
    file = open('destination.csv', 'w', newline='')
    writer = csv.writer(file)
    file.truncate()
    writer.writerow(location_save_list)
    writer.writerow(wp_km)
    writer.writerow(rate_s)
    writer.writerow(price_s)
    file.close()

    
    
    
    
add_button = ctk.CTkButton(master=app, text="+", command=add_location, width=10, height=10, corner_radius=50)  #Add waypoints
add_button.grid(row=2,column=3, padx=5, pady=5)   

clr_button = ctk.CTkButton(master=app, text="Clear All", command=clear) #Clear button
clr_button.grid(row=4, column =11, padx=20, pady=20, columnspan=1)

calc_button = ctk.CTkButton(master=app, text="Calculate", command=calculate) #Calculate button
calc_button.grid(row=4, column =10, padx=20, pady=20, columnspan=1)

start_label = ctk.CTkLabel(master=app, text = "Current Location") #Start label text
start_label.grid(row=0, column=0, padx=20, pady=20)

start = ctk.CTkEntry(master=app, placeholder_text="Current Location") #Start textbox
start.grid(row=0, column=1, padx=20, pady=20)

end_label = ctk.CTkLabel(master=app, text = "Destination") #Destination label text
end_label.grid(row=1, column=0, padx=20, pady=20)

end = ctk.CTkEntry(master=app, placeholder_text="Destination") #Destination TextBox
end.grid(row=1, column=1, padx=20, pady=20)

wp_label = ctk.CTkLabel(master=app, text = "WayPoints") #Waypoints label text
wp_label.grid(row=2, column=0, padx=20, pady=20)

wp = ctk.CTkEntry(master=app, placeholder_text="Waypoints") #Waypoints TextBox
wp.grid(row=2, column=1, padx=20, pady=20)

rate_options = ctk.CTkOptionMenu(master=app, values = ["Car","Van"],command=options)
rate_options.grid(row=4, column=0, padx=20, pady=20, columnspan=2)

rate_label = ctk.CTkLabel(master=app, text = "Rate per KM") #Rate label text
rate_label.grid(row=3, column=0, padx=20, pady=20)

rate = ctk.CTkEntry(master=app, placeholder_text="Vehicle") #Rate Texbox
rate.grid(row=3, column=1, padx=20, pady=20)

save = ctk.CTkButton(master=app, text = "Save", command=save)
save.grid(row=5, column=1, padx=20, pady=20, columnspan=10)



distance_box = ctk.CTkTextbox(master=app, width = 300, height=200) #Box which shows Distance
distance_box.grid(row=0,column=10, padx=20, pady=20, columnspan = 2, rowspan=3) 

total_distance_box = ctk.CTkTextbox(master=app, width = 300, height=60) #Box which shows Total Distance
total_distance_box.grid(row=3,column=10, padx=20, pady=20, columnspan = 2) 

app.mainloop()