class SpaceAge:
    PLANETS_EARTH_YEARS = [
        (planet, ratio * 31_557_600) for planet, ratio in (
            ('mercury', 0.2408467),
            ('venus', 0.61519726),
            ('earth', 1.0),
            ('mars', 1.8808158),
            ('jupiter', 11.862615),
            ('saturn', 29.447498),
            ('uranus', 84.016846),
            ('neptune', 164.79132),
)]
    def __init__(self, seconds):
        self.seconds = seconds
        for planet, ratio in self.PLANETS_EARTH_YEARS:
            setattr(self, 'on_' + planet, self._planet_years(ratio))

    def _planet_years(self, ratio):
        return lambda ratio=ratio: round(self.seconds/ratio, 2)