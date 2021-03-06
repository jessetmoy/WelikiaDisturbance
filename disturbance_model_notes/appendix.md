# Appendix

## Model Diagrams

## Fire Module Tables

### Custom Fuel Models





## Tree Allometry Tables

### Basal Area Growth Coefficients

|ID  |species        |b1       |b2       |b3      |BAL |
|----|---------------|---------|---------|--------|----|
|1   |american beech |0.0006911|0.0730441|0.013029|67  |
|2   |chestnut oak   |0.0008238|0.0790660|0.013762|63  |
|3   |eastern hemlock|0.0008737|0.0940538|0.009149|82  |
|4   |n. red oak     |0.0008920|0.0979702|0.018024|54  |
|5   |n.white-cedar  |0.0009050|0.0517297|0.012329|73  |
|6   |other hardwoods|0.0009567|0.1038458|0.020653|68  |
|7   |other pines    |0.0006634|0.1083470|0.016835|47  |
|8   |red maple      |0.0007906|0.0651982|0.016191|71  |



###Site Index Curve Parameters

|ID  |tree_species        |b1     |b2    |b3     |b4     |b5     |reference                         |
|----|--------------------|-------|------|-------|-------|-------|----------------------------------|
|1   |red maple           |2.9435 |0.9132|-0.0141|1.6580 |-0.1095|Carmean 1978                      |
|2   |sugar maple         |3.3721 |0.8407|-0.0150|2.6208 |-0.2661|Curtis and Post 1962, Solomon 1968|
|3   |sliver maple        |1.0645 |0.9918|-0.0812|1.7540 |-0.0272|Brendemuehl et al. 1961b          |
|4   |hickories           |1.8326 |1.0015|-0.0207|1.4080 |-0.0005|Boisen and Newlin 1910, Hampf 1965|
|5   |american beech      |29.7300|0.3631|-0.0127|16.7616|-0.6804|Carmean 1978                      |
|6   |upland oaks         |2.1037 |0.9140|-0.0275|3.7962 |-0.2530|Schnur 1937                       |
|7   |chestnut oak        |1.9044 |0.9752|-0.0161|0.9262 |0.0000 |Carmean 1971, 1972                |
|8   |atlantic white cedar|1.5341 |1.0013|-0.0208|0.9986 |-0.0012|Korstian and Bush 1931            |
|9   |eastern redcedar    |0.9276 |1.0591|-0.0424|0.3529 |0.3114 |Hampf 1965                        |
|10  |eastern white pine  |1.9660 |1.0000|-0.0240|1.8942 |0.0000 |Gevorkiantz 1957f                 |
|11  |jack pine           |1.6330 |1.0000|-0.0223|1.2419 |0.0000 |Gevorkiantz 1956c                 |
|12  |eastern hemlock     |2.1493 |0.9979|-0.0175|1.4086 |-0.0008|Frothingham 1915a                 |

### Bark Thickness Multipliers

| community                            | dominant tree species                     | vsp scaler  |
| ------------------------------------ | ----------------------------------------- | ----------: |
| Floodplain forest                    | avg(sliver maple, sycamore, American elm) | 0.032       |
| Red Maple Hardwood Swamp             | red maple                                 | 0.028       |
| Coastal Plain Atlantic Cedar Swamp   | Atlantic cedar                            | 0.025       |
| Pitch pine - scrub oak barrens       | avg( pitch pine, oak spp )                | 0.045       |
| Chestnut oak forest                  | avg( American chestnut, oak spp )         | 0.043       |
| Coastal oak beech forest             | avg( oak spp, beech )                     | 0.035       |
| Coastal oak hickory forest           | avg( oak spp, hickory spp )               | 0.045       |
| Oak tulip forest                     | avg( oak spp, yellow-poplar )             | 0.038       |
| Appalachian oak pine forest          | avg( oak spp, pine spp )                  | 0.038       |
| Hemlock northern hardwood forest     | hemlock                                   | 0.045       |
| Inland Atlantic Cedar Swamp          | Atlantic white cedar                      | 0.025       |
| Red maple black gum swamp            | avg( red maple, black gum )               | 0.034       |
| Red maple sweetgum swamp             | avg( red maple, sweetgum )                | 0.032       |
| Maritime holly forest                | holly                                     | 0.042       |
| Post oak black jack oak barrens      | post oak                                  | 0.044       |
| Appalachian oak hickory forest       | avg( oak spp, hickory spp )               | 0.045       |
| Beech maple mesic forest             | avg( beech, sugar maple )                 | 0.029       |
| Successional maritime hardwoods      | other hardwoods                           | 0.044       |
| Successional hardwood forest         | other hardwoods                           | 0.044       |


## Community Table

|     |Name                                                                    |type |fuel_c|fuel_m|fuel_n|max_canopy|forest|forest_shrub|obstruct|canopy_growth|to_ID|age_out|bark_thickness|site_index|tree_height_model|dbh_model|upland|succession_code|
|-----|------------------------------------------------------------------------|-----|------|------|------|----------|------|------------|--------|-------------|-----|-------|--------------|----------|-----------------|---------|------|---------------|
|-9999|No_Data                                                                 |-9999|-9999 |-9999 |-9999 |-9999     |-9999 |-9999       |-9999   |0            |     |       |              |          |                 |         |0     |               |
|60000|Deep_Water_Estuary                                                      |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60001|Deep_Coastal_Bay_Channels                                               |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60002|Deep_Coastal_Bay_Rock_Outcrops                                          |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60003|Deep_Coastal_Bay_Gravel_Bottom                                          |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60004|Deep_Coastal_Bay_Flats_Sand_Bottom                                      |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60005|Deep_Coastal_Bay_Flats_Mud_Bottom                                       |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60006|Deep_Coastal_Bay_Flats_Shell_Bottom                                     |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60007|Deep_Coastal_Bay_Flats_Rock_Bottom                                      |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60008|Shallow_Coastal_Bay_Channels                                            |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60009|Shallow_Coastal_Bay_Rock_Outcrops                                       |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60010|Shallow_Coastal_Bay_Flats_Gravel_Bottom                                 |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60011|Shallow_Coastal_Bay_Flats_Sand_Bottom                                   |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60012|Shallow_Coastal_Bay_Flats_Mud_Bottom                                    |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60013|Shallow_Coastal_Bay_Flats_Shell_Bottom                                  |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60014|Shallow_Coastal_Bay_Flats_Rock_Bottom                                   |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60015|Marine_Shallow_Water_Channel                                            |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60016|Marine_Shallow_Water_Rocks                                              |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60017|                                                                        |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60018|Deep_River_Dominated_Flats_Gravel_Bottom                                |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60019|Deep_River_Dominated_Flats_Sand_Bottom                                  |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60020|Deep_River_Dominated_Flats_Mud_Bottom                                   |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60021|Deep_River_Dominated_Flats_Shell_Bottom                                 |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60022|Deep_River_Dominated_Flats_Rock_Bottom                                  |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60023|Deep_River_Dominated_Estuary_Channels                                   |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60024|Deep_River_Dominated_Estuary_Rock_Outcrops                              |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60025|Shallow_River_Dominated_Estuary_Gravel_Bottom                           |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60026|Shallow_River_Dominated_Estuary_Shell_Bottom                            |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60027|Shallow_River_Dominated_Estuary_Rock_Bottom                             |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60028|Shallow_River_Dominated_Estuary_Sand_Bottom                             |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60029|Shallow_River_Dominated_Estuary_Mud_Bottom                              |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60030|Lagoonal_Shallow_Estuary_Gravel_Bottom                                  |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60031|Lagoonal_Shallow_Estuary_Shell_Bottom                                   |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60032|Lagoonal_Shallow_Estuary_Rock_Bottom                                    |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60033|Lagoonal_Shallow_Estuary_Sand_Bottom                                    |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60034|Lagoonal_Shallow_Estuary_Mud_Bottom                                     |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60100|Marine_Eelgrass_Meadow                                                  |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60200|Marine_Intertidal_Mudflat                                               |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60300|Marine_Intertidal_Gravel_Sand_Beach                                     |1    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60400|Marine_Rocky_Intertidal_Shore                                           |1    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60500|                                                                        |     |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60501|Deep_Tidal_River_Gravel_Bottom                                          |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60502|Deep_Tidal_River_Sand_Bottom                                            |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60503|Deep_Tidal_River_Mud_Bottom                                             |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60504|Deep_Tidal_River_Shell_Bottom                                           |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60505|Deep_Tidal_River_Rock_Bottom                                            |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60506|Shallow_Tidal_River_Gravel_Bottom                                       |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60507|Shallow_Tidal_River_Shell_Bottom                                        |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60508|Shallow_Tidal_River_Rock_Bottom                                         |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60509|Shallow_Tidal_River_Sand_Bottom                                         |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60510|Shallow_Tidal_River_Mud_Bottom                                          |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60600|                                                                        |     |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|60601|Deep_Saltwater_Tidal_Creek                                              |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60700|Brackish_Subtidal_Aquatic_Bed                                           |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60800|Low_Salt_Marsh                                                          |2    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|60900|High_Salt_Marsh                                                         |2    |14    |14    |14    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|61000|Salt_Panne                                                              |2    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|61100|Coastal_Salt_Pond                                                       |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|61200|Brackish_Tidal_Marsh                                                    |2    |14    |14    |14    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|61300|Brackish_Intertidal_Mudflats                                            |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|61400|Brackish_Intertidal_Shore                                               |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |0     |               |
|61500|Salt_Shrub                                                              |2    |15    |15    |15    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|61600|Midreach_Stream                                                         |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|61700|                                                                        |     |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|61701|Marsh_Headwater_Stream_Warm_Low_Gradient_Low_to_Moderately_Buffered     |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|61702|Marsh_Headwater_Stream_Warm_Low_Gradient_Moderately_to_Highly_Buffered  |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|61800|                                                                        |     |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|61801|Rocky_Headwater_Stream_Warm_High_Gradient_Low_to_Moderately_Buffered    |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|61802|Rocky_Headwater_Stream_Warm_High_Gradient_Highly_Buffered               |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|61803|Rocky_Headwater_Stream_Warm_Moderate_Gradient_Low_to_Moderately_Buffered|3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|61804|Rocky_Headwater_Stream_Warm_Moderate_Gradient_Highly_Buffered           |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|61900|Intermittent_Streams                                                    |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|62000|Coastal_Plain_Stream                                                    |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|62100|Coastal_Plain_Pond                                                      |4    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|62200|Eutrophic_Pond                                                          |4    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|62201|Beaver_Pond                                                             |4    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|62300|Deep_Emergent_Marsh                                                     |5    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|62400|Shallow_Emergent_Marsh                                                  |5    |14    |14    |14    |16        |0     |0           |0       |2            |62500|       |0.028         |58        |1                |8        |1     |1              |
|62500|Shrub_Swamp                                                             |5    |15    |15    |15    |50        |0     |0           |0       |1            |62900|       |0.028         |58        |1                |8        |1     |1              |
|62600|Coastal_Plain_Pond_Shore                                                |5    |15    |15    |15    |50        |0     |1           |0       |1            |73500|       |0.04          |30        |6                |6        |1     |1              |
|62700|Highbush_Blueberry_Bog_Thicket                                          |5    |15    |15    |15    |50        |0     |1           |0       |1            |73300|       |0.04          |30        |6                |6        |1     |1              |
|62800|Floodplain_Forest                                                       |5    |26    |27    |27    |90        |1     |0           |0       |1            |     |       |0.04          |61        |3                |6        |1     |               |
|62900|Red_Maple_Hardwood_Swamp                                                |5    |16    |16    |16    |90        |1     |0           |0       |1            |     |       |0.028         |58        |1                |8        |1     |               |
|63000|Vernal_Pool                                                             |5    |182   |182   |182   |80        |0     |0           |0       |1            |     |       |0.04          |61        |6                |6        |1     |               |
|63100|Coastal_Plain_Atlantic_Cedar_Swamp                                      |5    |16    |16    |16    |80        |1     |0           |0       |1            |     |       |0.25          |43        |8                |5        |1     |               |
|63200|Maritime_Beach                                                          |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|63300|Maritime_Dunes                                                          |6    |141   |141   |141   |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|63400|Maritime_Shrubland                                                      |6    |146   |146   |143   |50        |0     |1           |1       |1            |73500|       |0.04          |30        |6                |6        |1     |1              |
|63500|Hempstead_Plains_Grassland                                              |6    |123   |106   |103   |16        |0     |0           |0       |2            |64900|       |0.04          |61        |6                |6        |1     |1              |
|63600|Shoreline_Outcrop                                                       |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|63700|Calcareous_Shoreline_Outcrop                                            |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|63800|Cliff_Community                                                         |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|63900|Calcareous_Cliff_Community                                              |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|64000|Serpentine_Barrens                                                      |6    |124   |123   |103   |50        |0     |1           |1       |1            |     |       |0.04          |30        |6                |6        |1     |               |
|64100|Oak_Oppenings                                                           |6    |24    |25    |25    |60        |1     |1           |1       |1            |     |       |0.045         |30        |11               |7        |1     |               |
|64200|Chestnut_Oak_Forest                                                     |6    |17    |18    |19    |80        |1     |1           |1       |1            |     |       |0.043         |56        |7                |2        |1     |               |
|64300|Coastal_Oak_Beech_Forest                                                |6    |20    |21    |22    |100       |1     |1           |1       |1            |     |       |0.035         |60        |6                |4        |1     |               |
|64400|Coastal_Oak_Hickory_Forest                                              |6    |17    |18    |19    |90        |1     |1           |1       |1            |     |       |0.045         |60        |6                |4        |1     |               |
|64500|Oak_Tulip_Tree_Forest                                                   |6    |17    |18    |19    |100       |1     |1           |1       |1            |     |       |0.043         |60        |6                |4        |1     |               |
|64600|Appalachian_Oak_Pine_Forest                                             |6    |24    |25    |25    |75        |1     |1           |1       |1            |     |       |0.038         |60        |6                |4        |1     |               |
|64700|Hemlock_Northern_Hardwoods                                              |6    |189   |186   |182   |100       |1     |1           |1       |1            |     |       |0.045         |50        |12               |3        |1     |               |
|64800|Successional_Old_Field                                                  |6    |123   |106   |103   |16        |0     |0           |0       |2            |64900|       |0.04          |61        |6                |6        |1     |1              |
|64900|Successional_Shrubland                                                  |6    |148   |143   |146   |50        |0     |1           |1       |1            |73300|       |0.04          |61        |6                |6        |1     |1              |
|65000|Horticultural_Field                                                     |6    |103   |103   |103   |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|65100|Trail                                                                   |6    |189   |186   |182   |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|65200|Shell_Middens                                                           |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|65300|Wigwams_and_Longhouses                                                  |6    |163   |163   |163   |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|65400|Campsites                                                               |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|65500|Talus_Cave                                                              |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|65600|Calcareous_Talus_Cave                                                   |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|65700|Spring                                                                  |6    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|65801|Confined_River_Moderate_to_High_Gradient_Low_to_Moderately_Buffered     |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|65802|Confined_River_Moderate_to_High_Gradient_Well_Buffered                  |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|65803|Confined_River_Low_Gradient_Low_to_Moderately_Buffered                  |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|65804|Confined_River_Low_Gradient_Well_Buffered                               |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|70000|Brackish_Meadow                                                         |2    |14    |14    |14    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|70100|Sea_Level_Fen                                                           |5    |15    |15    |15    |16        |0     |0           |0       |1            |64900|       |0.04          |61        |6                |6        |1     |1              |
|70200|Brackish_Interdunal_Swale                                               |2    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|70300|Backwater_Slough                                                        |3    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|70400|Bog_Pond                                                                |4    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|70500|Oligotrophic_Pond                                                       |4    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|70600|Pine_Barrens_Shrub_Swamp                                                |5    |15    |15    |15    |50        |0     |0           |0       |1            |     |       |0.045         |57        |11               |7        |1     |               |
|70700|Oxbow_Pond                                                              |4    |98    |98    |98    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|70800|Coastal_Plain_Poor_Fen                                                  |5    |14    |14    |14    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|70900|Inland_Atlantic_Cedar_Swamp                                             |5    |16    |16    |16    |90        |1     |1           |0       |1            |     |       |0.025         |43        |8                |5        |1     |               |
|71000|Red_Maple_Black_Gum_Swamp                                               |5    |16    |16    |16    |90        |1     |1           |0       |1            |     |       |0.034         |58        |1                |8        |1     |               |
|71001|Red_Maple_SweetGum_Swamp                                                |5    |16    |16    |16    |90        |1     |1           |0       |1            |     |       |0.032         |58        |1                |8        |1     |               |
|71100|Rich_Shrub_Fen                                                          |5    |14    |14    |14    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|71200|Dwarf_Shrub_Bog                                                         |5    |15    |15    |15    |50        |0     |0           |0       |1            |62900|       |0.028         |58        |1                |8        |1     |1              |
|71300|Rich_Graminoid_Fen                                                      |5    |14    |14    |14    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|71400|Medium_Fen                                                              |5    |14    |14    |14    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|71500|Inland_Poor_Fen                                                         |5    |14    |14    |14    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |      |               |
|71600|Maritime_Holly_Forest                                                   |6    |146   |162   |144   |65        |1     |1           |1       |1            |     |       |0.042         |30        |6                |6        |1     |               |
|71700|Maritime_Pitch_Pine_Dunes                                               |6    |24    |25    |25    |65        |1     |1           |1       |1            |     |       |0.045         |30        |11               |7        |1     |               |
|71800|Maritime_Oak_Forest                                                     |6    |24    |25    |25    |65        |1     |1           |1       |1            |     |       |0.044         |30        |6                |4        |1     |               |
|71900|Maritime_Freshwater_Interdunal_Swale                                    |6    |14    |14    |14    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|72000|Maritime_Beech_Forest                                                   |6    |20    |21    |22    |65        |1     |1           |1       |1            |     |       |0.035         |35        |5                |1        |1     |               |
|72100|Maritime_Bluffs                                                         |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|72101|Rocky_Bluffs                                                            |6    |99    |99    |99    |0         |0     |0           |0       |0            |     |       |              |          |                 |         |1     |               |
|72200|Calcareous_Talus_Slope_Woodland                                         |6    |189   |186   |182   |60        |1     |1           |1       |1            |     |       |0.04          |61        |6                |6        |1     |               |
|72300|Acidic_Talus_Slope_Woodland                                             |6    |189   |186   |182   |60        |1     |1           |1       |1            |     |       |0.04          |61        |6                |6        |1     |               |
|72400|Post_Oak_Black_Jack_Oak_Barrens                                         |6    |146   |162   |144   |60        |1     |1           |1       |1            |     |       |0.044         |30        |6                |4        |1     |               |
|72500|Pitch_Pine_Oak_Forest                                                   |6    |24    |25    |25    |65        |1     |1           |1       |1            |     |       |0.045         |57        |11               |7        |1     |               |
|72600|Coastal_Oak_Laurel_Forest                                               |6    |17    |18    |19    |90        |1     |1           |1       |1            |     |       |0.045         |60        |6                |4        |1     |               |
|72700|Coastal_Oak_Heath_Forest                                                |6    |17    |18    |19    |90        |1     |1           |1       |1            |     |       |0.045         |60        |6                |4        |1     |               |
|72800|Appalachian_Oak_Hickory_Forest                                          |6    |17    |18    |19    |90        |1     |1           |1       |1            |     |       |0.045         |60        |6                |4        |1     |               |
|72900|Beech_Maple_Mesic_Forest                                                |6    |20    |21    |22    |100       |1     |1           |1       |1            |     |       |0.029         |57        |5                |1        |1     |               |
|73000|Successional_Fern_Meadow                                                |6    |123   |106   |103   |16        |0     |0           |1       |2            |     |       |0.04          |61        |6                |6        |1     |               |
|73100|Successional_Blueberry_Heath                                            |6    |148   |143   |146   |50        |0     |1           |1       |1            |     |       |0.04          |61        |6                |6        |1     |               |
|73200|Successional_Northern_Sandplain_Grasslands                              |6    |123   |106   |103   |16        |0     |0           |1       |2            |     |       |0.04          |61        |6                |6        |1     |               |
|73300|Successional_Northern_Hardwoods                                         |6    |189   |186   |182   |90        |1     |1           |1       |1            |     |50     |0.04          |61        |6                |6        |1     |2              |
|73400|Successional_Southern_Hardwoods                                         |6    |189   |186   |182   |90        |1     |1           |1       |1            |     |50     |0.04          |61        |6                |6        |1     |2              |
|73500|Successional_Maritime_Hardwoods                                         |6    |146   |146   |143   |90        |1     |1           |1       |1            |     |50     |0.04          |30        |6                |6        |1     |2              |
|73600|Maritime_Grassland                                                      |6    |123   |106   |103   |16        |0     |0           |0       |2            |64900|       |0.04          |61        |6                |6        |1     |               |
|73700|Maritime_Heathland                                                      |6    |123   |106   |103   |16        |0     |0           |0       |2            |64900|       |0.04          |61        |6                |6        |1     |               |
