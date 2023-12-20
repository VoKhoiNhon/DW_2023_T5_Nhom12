package model;

import java.time.LocalDateTime;

public class Weather {
    private LocalDateTime forecastday;
    private float temperatureMax;
    private String uvHealthConcernMax;
    private String weatherCodeMax;
    private String linkIMG;
    private float windSpeedAvg;
    private float humidityAvg;

    public Weather() {
    }

    public float getWindSpeedAvg() {
        return windSpeedAvg;
    }

    public void setWindSpeedAvg(float windSpeedAvg) {
        this.windSpeedAvg = windSpeedAvg;
    }

    public float getHumidityAvg() {
        return humidityAvg;
    }

    public void setHumidityAvg(float humidityAvg) {
        this.humidityAvg = humidityAvg;
    }

    public LocalDateTime getForecastday() {
        return forecastday;
    }

    public void setForecastday(LocalDateTime forecastday) {
        this.forecastday = forecastday;
    }

    public float getTemperatureMax() {
        return temperatureMax;
    }

    public void setTemperatureMax(float temperatureMax) {
        this.temperatureMax = temperatureMax;
    }

    public String getUvHealthConcernMax() {
        return uvHealthConcernMax;
    }

    public void setUvHealthConcernMax(String uvHealthConcernMax) {
        this.uvHealthConcernMax = uvHealthConcernMax;
    }

    public String getWeatherCodeMax() {
        return weatherCodeMax;
    }

    public void setWeatherCodeMax(String weatherCodeMax) {
        this.weatherCodeMax = weatherCodeMax;
    }

    public String getLinkIMG() {
        return linkIMG;
    }

    public void setLinkIMG(String linkIMG) {
        this.linkIMG = linkIMG;
    }

    @Override
    public String toString() {
        return "Weather{" +
                "forecastday=" + forecastday +
                ", temperatureMax=" + temperatureMax +
                ", uvHealthConcernMax='" + uvHealthConcernMax + '\'' +
                ", weatherCodeMax='" + weatherCodeMax + '\'' +
                ", linkIMG='" + linkIMG + '\'' +
                '}';
    }
}
