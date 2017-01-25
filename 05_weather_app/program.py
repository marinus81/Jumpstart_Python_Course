import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'temp, scale, cond, location')


def main():
    """
    The main programm

    :return:
    """

    print_headers()
    zipcode = get_zip_code()
    weather = get_html_page(zipcode)
    report = get_weather_from_html(weather)

    print('The weather in {} is {}. Current temperature: {} {}'.format(report.location, report.cond, report.temp, report.scale))
    # print_weather()


def print_headers():
    print('-------------------------------------------')
    print('              WEATHER APP')
    print('-------------------------------------------')
    print()


def get_zip_code():
    print('For which location do you want to know the weather?')
    zipcode = input('Please enter the ZIP code:')
    return zipcode


def get_html_page(zipcode):
    url = "https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}".format(zipcode)
    #    print(url)
    response = requests.get(url)
    #    print(response.text[0:250])
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    location = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    location = cleanup_text(location).split('\n')[0]
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(location=location, cond=condition, temp=temp, scale=scale)

    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
