class Purchase():
    def __init__(self, street, city, zip, state, beds, baths, sq__ft, type, sale_date, price, latitude, longitude):
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.beds = int(beds)
        self.baths = int(baths)
        self.sq__ft = int(sq__ft)
        self.type = type
        self.sale_date = sale_date
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    @staticmethod
    def from_dict(lookup):
        return Purchase(lookup['street'],
                        lookup['city'],
                        lookup['zip'],
                        lookup['state'],
                        lookup['beds'],
                        lookup['baths'],
                        lookup['sq__ft'],
                        lookup['type'],
                        lookup['sale_date'],
                        lookup['price'],
                        lookup['latitude'],
                        lookup['longitude'])