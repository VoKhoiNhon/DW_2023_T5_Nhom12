package controller;

import db.DBConnect;
import model.Weather;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;

@WebServlet(name = "weather", value = "/weather")
public class GetWeather extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println(request.getParameter("date"));
        String date = request.getParameter("date");
        Weather weather = DBConnect.getInstance().getWeather(date);
        response.getWriter().println("{" +
                "\"forecastday\":" + "\"" + weather.getForecastday().toLocalDate() + "\"" +
                ",\"temperatureMax\":" + "\"" + weather.getTemperatureMax() + "\"" +
                ",\"uvHealthConcernMax\":" + "\"" + weather.getUvHealthConcernMax() + "\"" +
                ",\"weatherCodeMax\":" + "\"" + weather.getWeatherCodeMax() + "\"" +
                ",\"linkIMG\":" + "\"" + weather.getLinkIMG() + "\"" +
                ",\"windSpeedAvg\":" + "\"" + weather.getWindSpeedAvg() + "\"" +
                ",\"humidityAvg\":" + "\"" + weather.getHumidityAvg() + "\"" +
                "}");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
