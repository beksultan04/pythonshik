class SpaceAge:
    EARTH_SECONDS = 365.25 * 24 * 60 * 60  # 31_557_600

    ORBITAL_PERIODS = {
        "earth": 1.0,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def _years_on(self, planet):
        years_on_earth = self.seconds / self.EARTH_SECONDS
        years_on_planet = years_on_earth / self.ORBITAL_PERIODS[planet]
        return round(years_on_planet, 2)

    def on_earth(self):
        return self._years_on("earth")

    def on_mercury(self):
        return self._years_on("mercury")

    def on_venus(self):
        return self._years_on("venus")

    def on_mars(self):
        return self._years_on("mars")

    def on_jupiter(self):
        return self._years_on("jupiter")

    def on_saturn(self):
        return self._years_on("saturn")

    def on_uranus(self):
        return self._years_on("uranus")

    def on_neptune(self):
        return self._years_on("neptune")
