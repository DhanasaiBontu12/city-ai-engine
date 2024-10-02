import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

# Step 3: Load the Dataset
def load_data():
    data = pd.read_csv('data/TrafficVolumeData.csv')  # Adjust the path if necessary
    data['date_time'] = pd.to_datetime(data['date_time'])  # Convert to datetime
    return data

traffic_data = load_data()  # Load the dataset when the application starts

# Step 4: Create Analysis Functions
def get_average_traffic_by_hour(data):
    data['hour'] = data['date_time'].dt.hour
    avg_traffic_by_hour = data.groupby('hour')['traffic_volume'].mean()
    return avg_traffic_by_hour

# Step 5: Create Plotting Function
def plot_average_traffic_by_hour(avg_traffic):
    plt.figure(figsize=(12, 6))
    avg_traffic.plot(kind='line')
    plt.title('Average Traffic Volume by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Average Traffic Volume')
    plt.grid()
    plt.savefig('static/plots/avg_traffic_by_hour.png')  # Save the plot
    plt.close()  # Close the plot to avoid display in Jupyter

# Step 6: Create Flask Route
@app.route('/')
def index():
    avg_traffic_by_hour = get_average_traffic_by_hour(traffic_data)
    plot_average_traffic_by_hour(avg_traffic_by_hour)
    return render_template('index.html')  # Render the HTML template

if __name__ == '__main__':
    app.run(debug=True)