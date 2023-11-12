from typing import Optional
from enum import Enum
"""
synodic period: The time taken between two successive oppositions or conjunctions of a celestial body, usually other planets within the solar system. 
sidereal period: The time taken for a celestial body to return to the same position on the celestial sphere.
inferior planet: A planet whose greatest elongation is less than 90 degrees (because they lie within Earth's orbit e.g. Mercury, Venus)
superior planet: A planet whose greatest elongation is as high as 180 degrees (becuase they lie outside of Earth's orbit e.g. Jupiter, Uranus)
"""


class Planet:
    __slots__ = "synodic_period", "is_superior", "sidereal_period"

    def __init__(self, synodic_period: Optional[float] = None, sidereal_period: Optional[float] = None,  is_superior: bool = False):
        self.synodic_period = synodic_period
        self.is_superior = is_superior
        self.sidereal_period = sidereal_period


class Planets(Planet):
    VENUS = Planet(synodic_period=583.9)
    EARTH = Planet(sidereal_period=365.26)
    MARS = Planet(synodic_period=780)
    JUPITER = Planet(synodic_period=399, is_superior=True)
    SATURN = Planet(synodic_period=378, is_superior=True)
    URANUS = Planet(synodic_period=370, is_superior=True)
    NEPTUNE = Planet(synodic_period=368, is_superior=True)
    PLUTO = Planet(synodic_period=367, is_superior=True)


def synodic_period(sidereal_period: float, is_superior: bool = False) -> str:
    ans: Optional[float] = None
    earth_sidereal_period = Planets.EARTH.sidereal_period

    if is_superior:
        ans = (sidereal_period * earth_sidereal_period) / \
            (sidereal_period - earth_sidereal_period)
    else:
        ans = (sidereal_period * earth_sidereal_period) / \
            (earth_sidereal_period - sidereal_period)
    return format(ans)


def sidereal_period(synodic_period: float, is_superior: bool = False) -> str:
    ans: Optional[float] = None
    earth_sidereal_period = Planets.EARTH.sidereal_period

    if is_superior:
        ans = (synodic_period * earth_sidereal_period) / \
            (synodic_period - earth_sidereal_period)
    else:
        ans = (synodic_period * earth_sidereal_period) / \
            (synodic_period + earth_sidereal_period)
    return format(ans)


def format(num: float) -> str:
    return f"{num} days/ {num/Planets.EARTH.sidereal_period} years"


if __name__ == "__main__":
    venus_sidereal_period = sidereal_period(Planets.VENUS.synodic_period)
    print("The sidereal period of venus is ", venus_sidereal_period)
    mars_sidereal_period = sidereal_period(
        Planets.MARS.synodic_period, is_superior=True)
    print("The sidereal period of mars is ", mars_sidereal_period)
