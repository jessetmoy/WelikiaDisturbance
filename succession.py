import os
import logging
import arcpy
import numpy as np
import pandas as pd
import scipy.stats as ss
import settings as s
import utils
import tree_allometry as ta


class Succession(object):

    def __init__(self, year):
        self.year = year
        self._ecocommunities_filename = 'ecocommunities_%s.tif'
        utils.set_arc_env(s.ecocommunities)

        self.canopy = None
        self.forest_age = None
        self.dbh = None
        self.ecocommunities = None
        self.climax_communities = arcpy.RasterToNumPyArray(s.ecocommunities)
        self.climax_canopy = None
        self.pond_time_since_disturbance = None
        self.garden_time_since_disturbance = None

        self.community_table = pd.read_csv(s.COMMUNITY_TABLE, index_col=0)
        self.dbh_lookup = pd.read_csv(s.DBH_LOOKUP, index_col=0)
        self.header, self.header_text, self.shape = utils.get_ascii_header(s.reference_ascii)
        self.set_ecocommunities()
        self.set_canopy()
        self.set_forest_age()
        self.set_dbh()

    def set_ecocommunities(self):
        this_year_ecocomms = os.path.join(s.OUTPUT_DIR, self._ecocommunities_filename % self.year)
        last_year_ecocomms = os.path.join(s.OUTPUT_DIR, self._ecocommunities_filename % (self.year - 1))

        if os.path.isfile(this_year_ecocomms):
            logging.info(this_year_ecocomms)
            ecocomm = arcpy.Raster(this_year_ecocomms)
            ecocomm.save(os.path.join(s.TEMP_DIR, 'ecosystems_before_RasterToNumPyArray_{}.tif'.format(self.year)))
            self.ecocommunities = arcpy.RasterToNumPyArray(this_year_ecocomms)

        elif os.path.isfile(last_year_ecocomms):
            logging.info(last_year_ecocomms)
            ecocomm = arcpy.Raster(last_year_ecocomms)
            ecocomm.save(os.path.join(s.TEMP_DIR, 'ecosystems_before_RasterToNumPyArray_{}.tif'.format(self.year)))
            self.ecocommunities = arcpy.RasterToNumPyArray(last_year_ecocomms)

        else:
            logging.info('initial run')
            logging.info(s.ecocommunities)
            self.ecocommunities = arcpy.RasterToNumPyArray(s.ecocommunities)

        # ecocomm = arcpy.NumPyArrayToRaster(self.ecocommunities,
        #                                    arcpy.Point(arcpy.env.extent.XMin, arcpy.env.extent.YMin),
        #                                    x_cell_size=s.CELL_SIZE,
        #                                    y_cell_size=s.CELL_SIZE)
        # ecocomm.save(os.path.join(s.TEMP_DIR, 'ecosystems_after_set_ecocommunities_{}.tif'.format(self.year)))

        self.shape = self.ecocommunities.shape

    def set_canopy(self):
        """
        set canopy for given year if no canopy raster exists, use previous year,
        else: initialize canopy raster
        :return:
        """

        if os.path.isfile(s.CANOPY):
            logging.info('Setting canopy')
            self.canopy = arcpy.RasterToNumPyArray(s.CANOPY)

        else:
            logging.info('Assigning initial values to canopy array')
            # if self.ecocommunities_array is None:
            #     self.ecocommunities_array = arcpy.RasterToNumPyArray(self.ecocommunities)

            self.canopy = np.empty(self.shape, dtype=np.int8)

            for index, row in self.community_table.iterrows():
                self.canopy[self.ecocommunities == index] = row.max_canopy

            canopy = arcpy.NumPyArrayToRaster(self.canopy,
                                              arcpy.Point(arcpy.env.extent.XMin, arcpy.env.extent.YMin),
                                              x_cell_size=s.CELL_SIZE,
                                              y_cell_size=s.CELL_SIZE)
            canopy.save(s.CANOPY)

    def set_forest_age(self):
        """
        set forest age for given year, if no forest age raster exists, use previous year,
        else: initialize froest age raster
        :return:
        """
        if os.path.isfile(s.FOREST_AGE):
            logging.info('Setting forest age')
            self.forest_age = arcpy.RasterToNumPyArray(s.FOREST_AGE)

        else:
            logging.info('Assigning initial values to forest age array')
            # if self.ecocommunities_array is None:
            #     self.ecocommunities_array = arcpy.RasterToNumPyArray(self.ecocommunities)

            # create truncated normal distrbution for age
            lower = s.MINIMUM_FOREST_AGE
            upper = s.MAXIMUM_FOREST_AGE
            mu = s.MEAN_INITIAL_FOREST_AGE
            sigma = s.AGE_VAR

            n = ss.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)

            # populate an array with ages from distribution
            tn = n.rvs(self.shape).astype(int)

            self.forest_age = np.empty(shape=self.shape, dtype=np.int32)

            for index, row in self.community_table.iterrows():
                if row.forest == 1:
                    self.forest_age = np.where(self.ecocommunities == index, tn, self.forest_age)

            forestage = arcpy.NumPyArrayToRaster(self.forest_age,
                                                 arcpy.Point(arcpy.env.extent.XMin, arcpy.env.extent.YMin),
                                                 x_cell_size=s.CELL_SIZE,
                                                 y_cell_size=s.CELL_SIZE)
            forestage.save(s.FOREST_AGE)

    def set_dbh(self):
        if os.path.isfile(s.DBH):
            logging.info('Setting dbh')
            self.dbh = arcpy.RasterToNumPyArray(s.DBH)

        else:
            logging.info('Assigning initial values to dbh array')
            self.dbh = np.zeros(shape=self.shape, dtype=np.float32)
            # self.dbh = np.empty(shape=self.shape, dtype=np.float16)

            for index, row in self.community_table.iterrows():
                if row.forest == 1:
                    age = np.ma.masked_where(self.ecocommunities != index, self.forest_age)
                    if s.DEBUG_MODE:
                        logging.info(index)
                    for a in np.ma.compressed(np.unique(age)):
                        if s.DEBUG_MODE:
                            logging.info(a)
                        d = self.dbh_lookup.ix[int(a)][str(index)]
                        self.dbh[(self.ecocommunities == index) & (self.forest_age == a)] = d

            dbh = arcpy.NumPyArrayToRaster(self.dbh,
                                           arcpy.Point(arcpy.env.extent.XMin, arcpy.env.extent.YMin),
                                           x_cell_size=s.CELL_SIZE,
                                           y_cell_size=s.CELL_SIZE)
            dbh.save(s.DBH)

    def grow(self):
        """
        for each upland community increment canopy, forest age and DBH
        :return:
        """
        for index, row in self.community_table.iterrows():
            canopy_growth = int(row['canopy_growth'])
            max_canopy = int(row['max_canopy'])

            # increment age of all communities that have trees all upland communities
            if row['forest'] == 1:
                # increment canopy
                self.canopy[(self.ecocommunities == index) & (self.canopy < max_canopy)] += canopy_growth

            elif max_canopy > 0 and row.forest == 0:
                # increment non forest canopy
                self.canopy[(self.ecocommunities == index)] += canopy_growth

            if max_canopy > 0:
                # increment forest age
                self.forest_age[self.ecocommunities == index] += 1

                # increment dbh
                if s.DEBUG_MODE:
                    logging.info("%s %s | max canopy: %s" % (index, row['Name'], max_canopy))
                self.dbh[(self.ecocommunities == index) &
                         (self.forest_age == 1)
                         & (self.dbh == 0)] = 0.5

                dbh_model = int(row['dbh_model'])
                site_index = int(row['site_index'])

                d_grow = ta.get_dgrow(species=dbh_model, site_index=site_index, dbh=self.dbh)

                self.dbh = np.where(self.ecocommunities == index, self.dbh + d_grow, self.dbh)

    def transition(self):
        """
        for each community type, transition the community to new state if conditions are met
        :return:
        """
        for index, row in self.community_table.iterrows():

            # CANOPY BASED SUCCESSION
            if row.succession_code == 1:
                self.ecocommunities[(self.ecocommunities == index) &
                                    (self.canopy > row['max_canopy'])] = row.to_ID

            # AGE BASED SUCCESSION
            elif row.succession_code == 2:
                self.ecocommunities = np.where((self.ecocommunities == index) &
                                               (self.forest_age > row['age_out']),
                                               self.climax_communities, self.ecocommunities)

    def run_succession(self):
        self.grow()
        self.transition()

        e = os.path.join(s.OUTPUT_DIR, self._ecocommunities_filename % self.year)
        ecocomm = arcpy.NumPyArrayToRaster(self.ecocommunities,
                                           arcpy.Point(arcpy.env.extent.XMin, arcpy.env.extent.YMin),
                                           x_cell_size=s.CELL_SIZE,
                                           y_cell_size=s.CELL_SIZE)
        # ecocomm.save(os.path.join(s.TEMP_DIR, 'ecosystems_after_succession_{}.tif'.format(self.year)))
        ecocomm.save(e)
        canopy = arcpy.NumPyArrayToRaster(self.canopy,
                                          arcpy.Point(arcpy.env.extent.XMin, arcpy.env.extent.YMin),
                                          x_cell_size=s.CELL_SIZE,
                                          y_cell_size=s.CELL_SIZE)
        canopy.save(s.CANOPY)
        forestage = arcpy.NumPyArrayToRaster(self.forest_age,
                                             arcpy.Point(arcpy.env.extent.XMin, arcpy.env.extent.YMin),
                                             x_cell_size=s.CELL_SIZE,
                                             y_cell_size=s.CELL_SIZE)
        forestage.save(s.FOREST_AGE)
        dbh = arcpy.NumPyArrayToRaster(self.dbh,
                                       arcpy.Point(arcpy.env.extent.XMin, arcpy.env.extent.YMin),
                                       x_cell_size=s.CELL_SIZE,
                                       y_cell_size=s.CELL_SIZE)
        dbh.save(s.DBH)

    # s1 = Succession(1508)
    # logging.info(s1.succession_table.head())
    # s1.run_succession()
    #
    # for index, row in s1.succession_table.iterrows():
    #     key = row['from_ID']
    #     logging.info(key, type(key))
    #     logging.info(row['max_canopy'])
    #     logging.info(row['to_ID'], type(row['to_ID']))
    # if key == 635:
    # self.communities[(self.communities == key) &
    #                  (self.canopy > row['max_canopy'])] = row['to_ID']

# logging.info('communities \n')
# logging.info(s1.communities)
# logging.info('canopy \n')
# logging.info(s1.canopy)
# run = range(0, 25)
# for year in run:
#     logging.info('year: %s' % year)
#     s1.grow()
#     s1.transition()
#     logging.info('communities \n')
#     logging.info(s1.communities)
#     logging.info('canopy \n')
#     logging.info(s1.canopy)
#
#     if year == max(run):
#         # communities
#         ax = plt.subplot(311)
#         ax.imshow(s1.communities, interpolation='none')
#         min_val, max_val = 0, s1.shape[0]
#         ind_array = np.arange(min_val, max_val, 1.0)
#         x, y = np.meshgrid(ind_array, ind_array)
#
#         for x_val, y_val, com in zip(x.flatten(), y.flatten(), s1.communities.flatten()):
#             c = int(com)
#             ax.text(x_val, y_val, c, va='center', ha='center', color='white')
#
#         # logging.info(s1.communities)
#         ax2 = plt.subplot(312)
#         ax2.imshow(s1.communities, interpolation='none')
#
#         # canopy
#         min_val, max_val = 0, s1.shape[0]
#         ind_array = np.arange(min_val, max_val, 1.0)
#         x, y = np.meshgrid(ind_array, ind_array)
#
#         for x_val, y_val, com in zip(x.flatten(), y.flatten(), s1.canopy.flatten()):
#             c = int(com)
#             ax2.text(x_val, y_val, c, va='center', ha='center', color='red')
#
#         ax2.imshow(s1.canopy, interpolation='none', cmap='Greens')
#
#         # forest age
#         ax3 = plt.subplot(313)
#         ax3.imshow(s1.forest_age, interpolation='none')
#         min_val, max_val = 0, s1.shape[0]
#         ind_array = np.arange(min_val, max_val, 1.0)
#         x, y = np.meshgrid(ind_array, ind_array)
#
#         for x_val, y_val, com in zip(x.flatten(), y.flatten(), s1.forest_age.flatten()):
#             c = int(com)
#             ax3.text(x_val, y_val, c, va='center', ha='center', color='red')
#
#         ax3.imshow(s1.forest_age, interpolation='none', cmap='Blues')
#         plt.show()
#         # logging.info(s1.canopy)
