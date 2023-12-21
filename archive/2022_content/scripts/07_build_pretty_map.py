# pip install osmnx
# pip install prettymaps

# pip install prettymapp
# inspo https://www.pythonmaps.com/gallery.html

import elevation
# clip the SRTM1 30m DEM of Rome and save it to Rome-DEM.tif
elevation.clip(bounds=(12.35, 41.8, 12.65, 42), output='Rome-DEM.tif')
# clean up stale temporary files and fix the cache in the event of a server error
elevation.clean()

#plot = prettymaps.plot('25 Watling Street, London, United Kingdom, EC4M 9BR')

#plot.savefig("map.jpg")

#from prettymapp.geo import get_aoi
#from prettymapp.osm import get_osm_geometries
#from prettymapp.plotting import Plot
#from prettymapp.settings import STYLES

#aoi = get_aoi(address="25 Watling Street, London, United Kingdom, EC4M 9BR", radius=1100, rectangular=False)
#df = get_osm_geometries(aoi=aoi)

#fig = Plot(
#    df=df,
#    aoi_bounds=aoi.bounds,
#    draw_settings=STYLES["Peach"]
#).plot_all()

#fig.savefig("map.jpg")