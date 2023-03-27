import pandas

# fourth_district = ['Aurora','Botocan', 'Camp Aguinaldo', 'Central', 'Damayang Lagi', 'Doña Imelda', 'Doña Josefa',
#                    'Don Manuel', 'Horseshoe', 'Immaculate Concepcion', 'Kalusugan', 'Kamuning', 'Kaunlaran',
#                    'Kristong Hari', 'Krus Na Ligas', 'Laging Handa', 'Malaya', 'Mariana', 'Obrero', 'Old Capitol '
#                                                                                                     'Site',
#                    'Paligsahan', 'Pinagkaisahan', 'Pinyahan', 'Roxas', 'Sacred Heart', 'San Isidro', 'San Martin de '
#                                                                                                      'Porres',
#                    'San Vicente', 'Santo Niño', 'Santol', 'Sikatuna Village', 'South Triangle', 'Tatalon',
#                    'Teachers Village East', 'Teachers Village West', 'U.P. Campus', 'U.P. Village', 'Valencia']
#
# ph_places = pandas.read_csv('python_PHL_adm3.csv')
# cities = ph_places.NAME_2.to_list()
# ph_baranggays = ph_places.NAME_3.to_list()
# print(len(fourth_district))
#
# # row_state = state_data[state_data.state_lower_case == answer_state_lowercase]
# # Benjamin_Math  = Report_Card.iloc[0]
#
# dist4_brgys = []
# for i in range(0, len(ph_baranggays)):
#     if ph_places.iloc[i].NAME_2 == 'Quezon City' and ph_places.iloc[i].NAME_3 in fourth_district:
#         # print(ph_places.iloc[i].NAME_3)
#         dist4_brgys.append(ph_places.iloc[i].NAME_3.lower())
#     else:
#         dist4_brgys.append('')
#         # if ph_places.iloc[i].NAME_3 in fourth_district:
#         #     print(ph_places.iloc[i].NAME_3)
#     # print(ph_places.iloc[i].NAME_3, ph_places.iloc[i].NAME_2)
# print(dist4_brgys)
# print(len(dist4_brgys))
# print(len(ph_baranggays))
#
# ph_places['district4_qc'] = dist4_brgys
# ph_places.to_csv('csv_ph_places')
#
# # list_cities = ['a','Quezon City','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
# #                'w','x','y','z',
# #              'a',
# #          'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','Quezon City','q','r','s','t','u','v','w','x',
# #                'y','z','a',\
# #     'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Quezon City']
# # list_baranggays =  ['a1','b1','c1','d1','e1','f1','g1','h1','i1','j1','k1','l1','m1','n1','o1','p1','q1','r1','s1','t1',
# #                 'u1','v1',
# #           'w1','x1','y1','z1','a',
# #          'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a2',
# #           'b2','c2','d2','e2','f2','g2','h2','i2','j2','k2','l2','m2','n2','o2','p2','q2','r2','s2','t2','u2','v2','w2',
# #           'x2','y2','z2']
# # list_4th_dist = ['a','e','i','o','u']
# #
# # for dist4 in list_4th_dist:
# #     for city in list_cities:
# #         for brgy in list_baranggays:
# #             if dist4 == brgy and city == 'Quezon City':
# #                 print(city, brgy, dist4)

lower_case_brgy = pandas.read_csv('district4_csv.csv')
print(lower_case_brgy.Baranggay)
conv_to_lowercase = []
for up_case in lower_case_brgy.Baranggay:
    print(up_case.lower())
    conv_to_lowercase.append(up_case.lower())
print(conv_to_lowercase)

lower_case_brgy['brgys_in_lowercase'] = conv_to_lowercase
print(lower_case_brgy)
print(type(lower_case_brgy))

lower_case_brgy.to_csv('final_brgy_list.csv')

# print(lower_case_brgy.iloc[0].brgys_in_lowercase)

# brgy_lowercase_list = lower_case_brgy.brgys_in_lowercase.to_list()
# for temp in brgy_lowercase_list:
#     if temp == 'dona josefa':
#         temp_index = brgy_lowercase_list.index(temp)
#         print(temp_index)
#         print(lower_case_brgy.iloc[temp_index]['x-coord'])
#         print(lower_case_brgy.iloc[temp_index]['y-coord'])