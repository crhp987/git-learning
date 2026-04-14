async function loadTraffic() {
    try {
        const response = await fetch("http://127.0.0.1:5000/traffic");
        const data = await response.json();

        document.getElementById("vehicles").innerText = data.vehicle_count;
        document.getElementById("signal").innerText = data.signal;

    } catch (error) {
        console.error("Error:", error);
    }
}

// auto load
loadTraffic();