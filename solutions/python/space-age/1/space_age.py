class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds 

    def on_mercury(self):
        earth_years = self.seconds / 31557600
        return round((earth_years / 0.2408467), 2)

    def on_venus(self):
        earth_years = self.seconds / 31557600
        return round((earth_years / 0.61519726), 2)

    def on_earth(self):
        earth_years = self.seconds / 31557600
        return round((earth_years / 1.0), 2)

    def on_mars(self):
        earth_years = self.seconds / 31557600
        return round((earth_years / 1.8808158), 2)

    def on_jupiter(self):
        earth_years = self.seconds / 31557600
        return round((earth_years / 11.862615), 2)

    def on_saturn(self):
        earth_years = self.seconds / 31557600
        return round((earth_years / 29.447498), 2)

    def on_uranus(self):
        earth_years = self.seconds / 31557600
        return round((earth_years / 84.016846), 2)

    def on_neptune(self):
        earth_years = self.seconds / 31557600
        return round((earth_years / 164.79132), 2)


    
