
clientID = "clientID - "+ Math.random(0, 1000)
host = "broker.emqx.io";
port = "8084"; //portti enkryptoiduille mqtt viesteille websockettien kautta



function Connect() {
    client = new Paho.MQTT.Client(host,Number(port), "/mqtt", clientID);
    client.onConnectionLost = onConnectionLost;
    
    client.connect({
        useSSL: true,
        onSuccess: Connected
    });
}

function Connected() {
    console.log("yhdistetty");
    btt = document.getElementById("spnButton"); 
    btt2 = document.getElementById("spnButton2");
    btt.removeAttribute("hidden"); // Hidden attribuutti poistetaan yhteyden muodostuksen jälkeen
    btt2.removeAttribute("hidden");
}

function onConnectionLost(responseObject) {
    Connect()
}

function publishMessage(msg) {
    topic = "tite24";

    Message = new Paho.MQTT.Message(msg)
    Message.destinationName = topic;

    client.send(Message);
}

