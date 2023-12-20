package db;

import model.Weather;

import java.sql.*;
import java.time.LocalDateTime;


public class DBConnect {
    String url = "jdbc:mysql://weatherforecastdata.mysql.database.azure.com:3306/datamart";
    String user = "weather";
    String pass = "dataserver123@";
    Connection connect;

    static DBConnect install;

    //kết nối với MySQL
    private DBConnect() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connect = DriverManager.getConnection(url, user, pass);
        } catch (ClassNotFoundException | SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public static DBConnect getInstance() {
        if (install == null) install = new DBConnect();
        return install;
    }

    //tạo đối tượng statement
    public Statement getStatement() {
        if (connect == null) return null;
        try {
            return connect.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);
        } catch (SQLException e) {
            return null;
        }
    }

    private void connect() throws SQLException, ClassNotFoundException {
        if (connect == null || connect.isClosed()) {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connect = DriverManager.getConnection(url, user, pass);
        }
    }

    public Connection get() {
        try {
            connect();
            return connect;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

    }

    public Weather getWeather(String time) {
        Weather result = null;
        try {
            CallableStatement callableStatement = getInstance().get().prepareCall("{call getWeatherData(?)}", ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);
            callableStatement.setDate(1, Date.valueOf(time));
            callableStatement.execute();
            ResultSet rs = callableStatement.getResultSet();
            rs.next();
            result = new Weather();
            result.setForecastday(rs.getTimestamp(1).toLocalDateTime());
            result.setTemperatureMax(rs.getFloat(2));
            result.setUvHealthConcernMax(rs.getString(3));
            result.setWeatherCodeMax(rs.getString(4));
            result.setLinkIMG(rs.getString(5));
            result.setWindSpeedAvg(rs.getFloat(6));
            result.setHumidityAvg(rs.getFloat(7));
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return result;
    }

    public static void main(String[] args) throws SQLException {
        System.out.println(getInstance().getWeather("2023-12-19"));
    }
}
