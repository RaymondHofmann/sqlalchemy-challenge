# Import dependencies
from flask import Flask, jsonify

# Create an app instance
app = Flask(__name__)

# Define the routes
@app.route('/')
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    """Convert the query results from your precipitation analysis to a dictionary."""
    

@app.route('/api/v1.0/stations')
def stations():
    """Return a JSON list of stations from the dataset."""
  

@app.route('/api/v1.0/tobs')
def tobs():
    """Query the dates and temperature observations of the most-active station for the previous year of data."""
    

@app.route('/api/v1.0/<start>')
def start(start):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date."""
    

@app.route('/api/v1.0/<start>/<end>')
def start_end(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start-end range."""
    

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
