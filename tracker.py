import time
import win32gui
import csv
from datetime import datetime

def main(): 
    try:
        last_title = None
        start_time = datetime.now()

        #main loop
        while True:
            window = win32gui.GetForegroundWindow()
            title = win32gui.GetWindowText(window)
            hyphen_count = title.count("- ")

            parsed_title = title_parsing( title, hyphen_count) #send it to get parsed

            #if not able to access the string then set a message
            if not parsed_title or parsed_title.isspace():
                parsed_title = "Could not access window title"


            if parsed_title != last_title:
                if last_title is not None:
                    end_time = datetime.now()
                    duration = int((end_time - start_time).total_seconds())
            
                    session_logging_blueprint(last_title, duration, start_time, end_time)
                    calculated_sessions = session_time_calculation()
                    duration_logging = session_duration_logging(calculated_sessions)

                last_title = parsed_title
                start_time = datetime.now()

            

            time.sleep(1)  # Check every second


    except KeyboardInterrupt:
        print("LOGGING STOPPED")
        #calculate the data for the window the user was last active on so we dont lose it
        if last_title is not None:
                    end_time = datetime.now()
                    duration = int((end_time - start_time).total_seconds())
            
                    session_logging_blueprint(last_title, duration, start_time, end_time)
                    last_session = session_time_calculation()
                    last_log = session_duration_logging(last_session)



def title_parsing(title, hyphen_count):
    if hyphen_count == 1:
        _, title_name = title.split("- ")
        return title_name

    elif hyphen_count == 2:
        _, _, title_name = title.split("- ")
        return title_name

    elif hyphen_count == 0:
        return title 

    else:
        _, _, _, title_name = title.split("- ") 
        return title_name 


def active_session_logging(header, data_format, file_name):
    # also learnt that newline parameter removes extra spaces and logs clearly on each line
    # encoding parameter makes sure that every character is understood by python 
    try:
        with open(file_name, "x", newline='', encoding='utf-8') as file: # x means it will create a file if it does not exist so we dont have ti create a file everytime, if it exists
            writer = csv.writer(file)               # it will raise file exists error 
            writer.writerow(header) #creates heading

    except FileExistsError:
        pass
    
    #appends the csv with new sessions in each row
    with open(file_name, "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data_format)


def session_logging_blueprint(title, duration, start_time, end_time, file_name="session_logs.csv"):
    header = ["TITLE", "DURATION in sec", "START_TIME", "END_TIME"]
    data_format = [title, duration, start_time.strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S")]
    
    active_session_logging(header, data_format, file_name)



def session_time_calculation(file_name="session_logs.csv"):

    totals = {} #empty dictionary to store the window name and the time duration

    with open(file_name, "r", newline='', encoding='utf-8') as reading:
        reader = csv.DictReader(reading)  
        for row in reader:
            title = row["TITLE"]
            duration = int(row["DURATION in sec"]) #access the title and the duration
            if title in totals :
                totals[title] += duration #add to the dictionary as key value pairs
            else:
                totals[title] = duration

    return totals

def session_duration_logging(sessions, file_name="session_durarion.csv"):
    try:
        with open(file_name, "w", newline='', encoding='utf-8') as file: #open another file to store the final durations
            writer = csv.writer(file)  #we use w here because it needs to be re written everytime
            writer.writerow(["TTILE", "TOTAL DURATION in sec"])   #with new calculations
            for title in sessions:
                writer.writerow([title, sessions[title]])

    except FileNotFoundError:
        pass  

    
if __name__ == "__main__":
    main()