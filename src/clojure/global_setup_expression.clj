;; Create a socket for sending UDP to Python, and record the
;; address and port to which such UDP messages should be sent.
(swap! globals assoc :py-socket (java.net.DatagramSocket.))
(swap! globals assoc :py-address (java.net.InetAddress/getLocalHost))
(swap! globals assoc :py-port 7001)