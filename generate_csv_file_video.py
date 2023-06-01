import datetime
import csv
def generate_csv_file_video(Id):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    filename = "Timestamp_video.csv"
    with open(filename, 'w', newline='') as file:
        # Create a CSV writer object
        print("yo")
        writer = csv.writer(file)
        writer.writerow(['Timestamp_video',"id" ])
        writer.writerow([timestamp, Id])