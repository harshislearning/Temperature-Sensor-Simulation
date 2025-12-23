const latestTempEl = document.getElementById("latest-temp");
const latestTimeEl = document.getElementById("latest-time");
const measurementsEl = document.getElementById("measurements");

const wsProtocol = window.location.protocol === "https:" ? "wss" : "ws";
const wsUrl = wsProtocol + "://" + window.location.host + "/ws";
const socket = new WebSocket(wsUrl);

socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    latestTempEl.textContent = data.temperature;
    latestTimeEl.textContent = data.timestamp;

    const li = document.createElement("li");
    li.textContent = `Temp: ${data.temperature} °C, Time: ${data.timestamp}`;
    measurementsEl.insertBefore(li, measurementsEl.firstChild);

    const maxItems = 20;
    while (measurementsEl.children.length > maxItems) {
        measurementsEl.removeChild(measurementsEl.lastChild);
    }
};

socket.onopen = function () {
    socket.send("hello");
};
