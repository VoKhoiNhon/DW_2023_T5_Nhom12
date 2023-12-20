<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style/reset.css">
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">

    <!-- Vanilla Datepicker CSS -->
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/vanillajs-datepicker@1.1.4/dist/css/datepicker.min.css'>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <link rel="stylesheet" href="style/style.css">

</head>

<body>
<div class="content">
    <div class="title-group position-absolute top-0 start-50 translate-middle-x">
        <img src="images/sunny-cloud.png" alt="sunny-cloud" class="title-icon">
        <h1 class="title-text">WeatherHCM</h1>
    </div>
    <div class="input-group mb-4">
        <input id="datepicker_input" type="text" class="datepicker_input form-control" placeholder="Choose Date"
               required aria-label="">
    </div>
    <div class="position-absolute bottom-0 start-50 translate-middle-x panel"
         style="box-sizing: border-box; padding-bottom: 50px">
        <i class="arrow-left fa-solid fa-chevron-left fa-2xl" style="cursor: pointer"></i>
        <div class="slider-item ">
            <div class="top">
                <i class="fa-solid fa-location-dot fa-2xl" style="margin-top: 25px;"></i>
                <span class="temperature">
                        <span id="temperature-avg" class="number-temperature">27</span>
                        <span class="cur-temperature">°C</span>
                    </span>
                <i class="fa-solid fa-temperature-half fa-2xl " style="margin-top: 25px;"></i>
            </div>
            <div class="mid">
                <span id="forecastday" class="date-time"></span>
                <img id="link-img-weather" src="images/clould.png" alt="" class="icon">
            </div>
            <table>
                <tr>
                    <th>UV CONCERN</th>
                    <th>WEATHER</th>
                    <th>HUMIDITY</th>
                    <th>WIND</th>
                </tr>
                <tr>
                    <td id="uv-health-concern-max">0</td>
                    <td id="weather-code-max">0</td>
                    <td id="humidity-avg">0</td>
                    <td id="wind-speed-avg">0</td>
                </tr>

            </table>
        </div>
        <i class="arrow-right fa-solid fa-chevron-right fa-2xl" style="cursor: pointer"></i>
    </div>
</div>

<!-- Bootstrap 5 JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj"
        crossorigin="anonymous"></script>
<script type="text/javascript" src="//code.jquery.com/jquery-1.11.0.min.js"></script>
<script type="text/javascript" src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
<!-- Vanilla Datepicker JS -->
<script src='https://cdn.jsdelivr.net/npm/vanillajs-datepicker@1.1.4/dist/js/datepicker-full.min.js'></script>
<script type="text/javascript" src="//cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>
<%--<script src="js/main.js"></script>--%>
<script>
    let nowDate = formatDate(Date.now());
    $(document).ready(function () {
        document.getElementById('datepicker_input').value = nowDate;
        const getDatePickerTitle = elem => {
            const label = elem.nextElementSibling;
            let titleText = '';
            if (label && label.tagName === 'LABEL') {
                titleText = label.textContent;
            } else {
                titleText = elem.getAttribute('aria-label') || '';
            }
            return titleText;
        }

        const elems = document.querySelectorAll('.datepicker_input');
        for (const elem of elems) {
            const datepicker = new Datepicker(elem, {
                'format': 'yyyy-mm-dd', // UK format
                title: getDatePickerTitle(elem)
            });
        }
        callAPIWeather(formatDate(Date.now()))

        $('.datepicker-cell.day').click(function () {
            const date = $(this).attr('data-date');
            nowDate = formatDate(new Date(parseInt(date)));
            callAPIWeather(nowDate);
        });

        $('.arrow-left').click(function () {
            nowDate = subtractDays(nowDate, 1);
            callAPIWeather(nowDate);
            $('.datepicker_input').val(nowDate);
        })

        $('.arrow-right').click(function () {
            nowDate = addDays(nowDate, 1);
            callAPIWeather(nowDate);
            $('.datepicker_input').val(nowDate)
        })

    });


    function formatDate(date) {
        let d = new Date(date),
            month = '' + (d.getMonth() + 1),
            day = '' + (d.getDate()),
            year = d.getFullYear();
        return [year, month, day].join('-');
    }

    function addDays(inputDate, daysToAdd) {
        let date = new Date(inputDate);
        date.setDate(date.getDate() + daysToAdd);
        return date.toISOString().slice(0, 10);
    }

    function subtractDays(inputDate, daysToSubtract) {
        let date = new Date(inputDate);
        date.setDate(date.getDate() - daysToSubtract);
        return date.toISOString().slice(0, 10);
    }

    function callAPIWeather(date) {
        $.ajax({
            url: '/weather',
            method: 'GET',
            data: {date: date},
            success: function (data) {
                let a = JSON.parse(data);
                const forecastday = a.forecastday;
                const temperatureAvg = a.temperatureMax;
                const uvHealthConcernMax = a.uvHealthConcernMax;
                const weatherCodeMax = a.weatherCodeMax;
                const linkIMG = a.linkIMG;

                document.getElementById('temperature-avg').innerHTML = temperatureAvg;
                document.getElementById('forecastday').innerHTML = forecastday;
                document.getElementById('uv-health-concern-max').innerHTML = uvHealthConcernMax;
                document.getElementById('weather-code-max').innerHTML = weatherCodeMax;
                document.getElementById('link-img-weather').src = linkIMG;
                document.getElementById('humidity-avg').innerHTML = a.humidityAvg;
                document.getElementById('wind-speed-avg').innerHTML = a.windSpeedAvg;
            }
        });
    }
</script>
</body>

</html>