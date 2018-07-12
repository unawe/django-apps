from activities.models import MetadataOption


def add(group, code, title, position):
    x = MetadataOption(group=group, code=code, title=title, position=position)
    x.save()



i = 0
i+=1; add('content_area_focus', 'astronomy', u'Astronomy', i)
i+=1; add('content_area_focus', 'earth_science', u'Earth Science', i)
i+=1; add('content_area_focus', 'other', u'Other', i)

i=0
i+=1; add('astronomical_categories', 'astronomical_instrumentation', 'Astronomical instrumentation', i)
i+=1; add('astronomical_categories', 'astronomical_databases', 'Astronomical databases', i)
i+=1; add('astronomical_categories', 'astrometry_and_celestial_mechanics', 'Astrometry and celestial mechanics', i)
i+=1; add('astronomical_categories', 'the_sun', 'The Sun', i)
i+=1; add('astronomical_categories', 'planetary_systems', 'Planetary systems', i)
i+=1; add('astronomical_categories', 'stars', 'Stars', i)
i+=1; add('astronomical_categories', 'interstellar_medium_(ISM)', 'Interstellar medium (ISM)', i)
i+=1; add('astronomical_categories', 'nebulae', 'Nebulae', i)
i+=1; add('astronomical_categories', 'the_milky_way', 'The Milky Way', i)
i+=1; add('astronomical_categories', 'galaxies', 'Galaxies', i)
i+=1; add('astronomical_categories', 'cosmology', 'Cosmology', i)

i=0
i+=1; add('earth_science', 'geoscience', 'Geoscience', i)
i+=1; add('earth_science', 'geophysics', 'Geophysics', i)
i+=1; add('earth_science', 'soil science', 'Soil science', i)
i+=1; add('earth_science', 'ecology', 'Ecology', i)
i+=1; add('earth_science', 'hydrology', 'Hydrology', i)
i+=1; add('earth_science', 'glaciology', 'Glaciology', i)
i+=1; add('earth_science', 'atmospheric sciences', 'Atmospheric Sciences', i)
i+=1; add('earth_science', 'volcanologist', 'Volcanologist', i)
i+=1; add('earth_science', 'geography', 'Geography', i)
i+=1; add('earth_science', 'oceanography', 'Oceanography', i)

i+0
i+=1; add('space_science', 'robotic spaceflight', 'Robotic Spaceflight', i)
i+=1; add('space_science', 'human spaceflight', 'Human Spaceflight', i)
i+=1; add('space_science', 'communications', 'Communications', i)
i+=1; add('space_science', 'orbital mechanics', 'Orbital Mechanics', i)
i+=1; add('space_science', 'aerospace engineering', 'Aerospace Engineering', i)
i+=1; add('space_science', 'low gravity', 'Low gravity', i)
i+=1; add('space_science', 'astrobiology', 'Astrobiology', i)
i+=1; add('space_science', 'space habitation', 'Space Habitation', i)
i+=1; add('space_science', 'remote sensing', 'Remote sensing', i)
i+=1; add('space_science', 'robotics', 'Robotics', i)