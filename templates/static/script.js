fetch('https://api.openweathermap.org/data/2.5/weather?q=LOCATION&appid=06f37b1bf31beb8060501481105fd6c5')
    .then(response => response.json())
    .then(data => {
        const weatherInfo = document.getElementById('weather-info');
        const temperature = Math.round(data.main.temp - 273.15); // Convert temperature from Kelvin to Celsius
        weatherInfo.textContent = `Temperature: ${temperature}°C, Condition: ${data.weather[0].description}`;
    })
    .catch(error => {
        console.error('Error fetching weather data:', error);
        const weatherInfo = document.getElementById('weather-info');
        weatherInfo.textContent = 'Failed to fetch weather data';
    });

// Time update logic
function updateTime() {
    const timeInfo = document.getElementById('time-info');
    const currentTime = new Date();
    const formattedTime = currentTime.toLocaleTimeString();
    timeInfo.textContent = `Current time: ${formattedTime}`;
}

setInterval(updateTime, 1000); // Update time every second

// Date update logic
function updateDate() {
    const dateInfo = document.getElementById('date-info');
    const currentDate = new Date();
    const formattedDate = currentDate.toLocaleDateString();
    dateInfo.textContent = `Current date: ${formattedDate}`;
}

updateDate(); // Update date initially
setInterval(updateDate, 60000); // Update date every minute
