(defn send-json-to-python
  "Encodes a map as JSON and sends it in a UDP packet
  to Python."
  [globals m]
  (let [message (str (cheshire.core/encode m) "\n")  ; Encode as JSON line.
       {:keys [py-address py-port py-socket]} @globals  ; Find where to send.
       data (.getBytes message)  ; Get JSON as raw byte array.
       packet (java.net.DatagramPacket. data (count data) py-address py-port)]
  (.send py-socket packet)))

(add-library '[org.clojure/data.json "2.4.0"])
(require '[clojure.data.json :as json])