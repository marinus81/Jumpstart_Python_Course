def main():
    """
    The main programm

    :return:
    """

    print_headers()
    zipcode=get_zip_code()
    weather=get_html_page(zipcode)
    #print_weather()


def print_headers():
    print('-------------------------------------------')
    print('              WEATHER APP')
    print('-------------------------------------------')
    print()


def get_zip_code():
    print('For which location do you want to know the weather?')
    zipcode=input('Please enter the ZIP code:')
    return zipcode

def get_html_page(zipcode):
    url="https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}".format(zipcode)
    print(url)

if __name__ == '__main__':
    main()