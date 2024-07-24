import mysql.connector
from mysql.connector import Error

# local database configuration
config = {
    'user': 'v078803',
    'password': 'HibaIrinaPuyaHeiko2024_',
    'host': 'localhost/',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'v078803',
    'raise_on_warnings': True
}

# global variables for track data and track history
track_data = {}
track_history = {}

# Placeholder für Socket.IO (The actual Socket.IO initialisation must take place here)
class Socket:
    def emit(self, event, data):
        print(f"Event: {event}, Data: {data}")

socketio = Socket()

def convert_time(milliseconds):
    # Converts milliseconds into a minutes:seconds format
    seconds = milliseconds / 1000
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"

def update_track_info(json_data):
    # Updates the track information, sends it via Socket.IO and saves it in the MySQL database and in the history
    global track_data, track_history
    track_data = {
        "track_artist": json_data.get("artist"),
        "track_bpm": round(json_data.get("bpm"), 2) if json_data.get("bpm") is not None else None,
        "track_device": json_data.get("device"),
        "track_genre": json_data.get("track_genre"),
        "track_key": json_data.get("key"),
        "track_label": json_data.get("label"),
        "track_timestamp": json_data.get("timestamp")[:19],
        "track_title": json_data.get("title"),
        "rekordbox_id": json_data.get("id")
    }
    
    socketio.emit('update', track_data)
    save_to_database(track_data)
    add_to_history(track_data)

def save_to_database(track_data):
    # connection to local MySQL-Server and insert track data
    try:
        db_connection = mysql.connector.connect(**config)
        
        if db_connection.is_connected():
            print ("MySQL connection established")
            cursor = db_connection.cursor()
            insert_query = """
                INSERT INTO playlist (track_artist, track_bpm, track_device, track_genre, track_key, track_label, track_timestamp, track_title, rekordbox_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            track_data_tuple = (
                track_data["track_artist"],
                track_data["track_bpm"],
                track_data["track_device"],
                track_data["track_genre"],
                track_data["track_key"],
                track_data["track_label"],
                track_data["track_timestamp"],
                track_data["track_title"],
                track_data["rekordbox_id"]
            )
            print ("Timestamp",track_data["track_timestamp"])
            cursor.execute(insert_query, track_data_tuple)
            db_connection.commit()
            print("Track data successfully written to the database")
    except Error as e:
        print("Error connecting to the MySQL database", e)
    finally:
        if (db_connection.is_connected()):
            cursor.close()
            db_connection.close()
            print("MySQL connection closed")

def add_to_history(track_data):
    # Adds the track data to the track history
    global track_history
    track_id = track_data["rekordbox_id"]
    track_history[track_id] = track_data
    print("Track data successfully added to history", track_history)