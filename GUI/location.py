from geopy import geocoders  
gn = geocoders.GeoNames()

print(gn.geocode("Cleveland, OH 44106"))
# (u'Cleveland, OH, US', (41.4994954, -81.6954088))

print(gn.geocode("Cleveland, OH", exactly_one=False)[0])
# (u'Cleveland, OH, US', (41.4994954, -81.6954088))