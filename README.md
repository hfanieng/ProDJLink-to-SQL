# ProDJLink Data Logger

## Project description

This project reads data from the ProDJLink network with [Beat Link Trigger][1], sends it via UDP to a Python script and then saves the data in a SQL database.

> **Disclaimer**: This project is **not** affiliated with Pioneer Corp. or its related companies in any way and has been written independently! ProDJLink to SQL is licensed under the [MIT license][license-link]. The maintainers of the project are not liable for any damages to your data cause this is an experimintal project.

## Table of contents

1. Introduction
2. Requirements
3. Installation
4. Usage
5. Configuration
6. Database structure
7. Troubleshooting
8. Equipment

## Introduction

Inspired by a part in the great manual of Beat Link Trigger about [writing played songs in a textfile][2] i want to store my played songs from the [Pioneer XDJ-XZ][3] in a database.

One further option is to show the playlist on Website that is connected to a MySQL-Database.

## Requirements

- Full ProDJLink compatible Hardware
- Beat Link Trigger
- Python 3.x
- SQL database (e.g. MySQL, PostgreSQL)
- UDP support

> Without compatible hardware, the simulation mode can be used in the Update Track Expressions of the trigger

## Installation

Steps to install the required software and libraries:

1. clone this repository: `git clone https://github.com/hfanieng/ProDJLink-to-SQL`
2. install the Python dependencies:  
`pip install mysql.connector`  
`pip install socket`  
`pip install json`  
`pip install threading`

3. configure the SQL database (see configuration)

## Usage

Instructions for using the project:

1. start Beat Link Trigger and configure it to send data over UDP.
2. run the Python script: `python main.py`
3. check the SQL database for the stored data.

## Configuration

1. Beat Link Trigger

    - Edit Shared Functions:

    ```clojure
    (defn send-json-to-python
    ;"Encodes a map as JSON and sends it in a UDP packet to Python."
    [globals m]
    (let [message (str (cheshire.core/encode m) "\n")  ; Encode as JSON line.
        {:keys [py-address py-port py-socket]} @globals  ; Find where to send.
        data (.getBytes message)  ; Get JSON as raw byte array.
        packet (java.net.DatagramPacket. data (count data) py-address py-port)]
    (.send py-socket packet)))
    ```

    - Edit Global Setup Expression:

    ```clojure
    ;; Create a socket for sending UDP to Python, and record the
    ;; address and port to which such UDP messages should be sent.
    (swap! globals assoc :py-socket (java.net.DatagramSocket.))
    (swap! globals assoc :py-address (java.net.InetAddress/getLocalHost))
    (swap! globals assoc :py-port 7001)
    ```

    - Set up a Trigger that is configured to watch the Master Player, and install the following Tracked Update Expression:

    ![Interface][5]

    ```clojure
    (import '[java.net DatagramSocket DatagramPacket InetAddress])

    (defn send-udp [host port message]
    (let [socket (DatagramSocket.)
        address (InetAddress/getByName host)
        buffer (.getBytes message)
        packet (DatagramPacket. buffer (count buffer) address port)]
    (.send socket packet)
    (.close socket)))

    (when trigger-active?
    (when (not= track-metadata (:last-track @locals))
        (swap! locals assoc :last-track track-metadata)
        (when (some? track-metadata)
            (let [log-entry (json/write-str
                        {:timestamp (str (java.time.LocalDateTime/now))
                        :device device-name
                        :artist track-artist
                        :id rekordbox-id
                        :title track-title
                        :label track-label
                        :bpm effective-tempo}
                        :escape-slash false)
            udp-host "127.0.0.1"  ; target host
            udp-port 7001]       ; target port
        (send-udp udp-host udp-port log-entry)))))
    ```

2. Database structure

    ```mermaid
    erDiagram
    playlist {
        INT track_id PK
        VARCHAR track_artist
        FLOAT track_bpm
        VARCHAR track_device
        VARCHAR track_genre
        VARCHAR track_key
        VARCHAR track_label
        TIMESTAMP track_timestamp
        VARCHAR track_title
        INT rekordbox_id FK
    }
    ```

The rekordbox_id is for further use as a foreign key.

Example for a successful done entry in the database:

## Troubleshooting

Common problems and their solutions:

- On MacOS the Python-Script works and writes the data in the table, on Windows it runs into an error due to the length of the timestamp.

## Equipment used for the project

All tests runs with the old but great [Pioneer XDJ-XZ][3] with ❤️ and 🤩 at my hometown [Hagen-Wehringhausen][7].![XDJ-XZ][6]

[1]:<https://github.com/Deep-Symmetry/beat-link-trigger>
[2]:<https://blt-guide.deepsymmetry.org/beat-link-trigger/7.4.1/Matching.html#writing-a-playlist>
[3]:<https://www.pioneerdj.com/en/product/all-in-one-system/xdj-xz/black/overview/>
[5]:docs/images/Beat_Link_Triggers_interface_screenshot_Software_Interface.png
[6]:<https://www.pioneerdj.com/-/media/pioneerdj/images/products/all-in-one-system/xdj-xz/xdj-xz_prm_top.png?h=1316&w=1792&hash=CDDC51D731D7571112C6D6AB25B04626>
[7]: <https://de.wikipedia.org/wiki/Wehringhausen>
[license-link]: https://github.com/hfanieng/ProDJLink-to-SQL/blob/main/LICENSE
