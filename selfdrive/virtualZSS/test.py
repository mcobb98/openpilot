import time
from selfdrive.virtualZSS import virtualZSS_wrapper
virtualZSS_model = virtualZSS_wrapper.get_wrapper()
virtualZSS_model.init_model()
'''start = time.time()
for i in range(30):
 model_output = virtualZSS_model.run_model(0.8653078153514447,
  0.46805728618371273,
  0.46805728618371273,
  0.28780443294609244,
  0.01075646532123655)
print(time.time() - startl)'''
for i in range(1000):
  model_output = virtualZSS_model.run_model_lstm([0.72887384, 0.69831158, 0.6034188, 0.72869553, 0.6981483,
                                          0.6042735, 0.72910522, 0.69848449, 0.60512821, 0.72911018,
                                          0.70135591, 0.60598291, 0.72905472, 0.70128567, 0.60683761,
                                          0.72942636, 0.69876334, 0.60683761, 0.72976182, 0.70189068,
                                          0.60769231, 0.72983983, 0.70195488, 0.60854701, 0.73005174,
                                          0.70218076, 0.60854701, 0.73001669, 0.70216653, 0.60940171,
                                          0.73020394, 0.70233799, 0.61025641, 0.73060646, 0.70271022,
                                          0.61111111, 0.73079637, 0.70284178, 0.61196581, 0.73087294,
                                          0.70295089, 0.61196581, 0.73103641, 0.70311433, 0.61282051,
                                          0.73128585, 0.70324624, 0.61367521, 0.73114485, 0.70322657,
                                          0.61452991, 0.7318116, 0.70374223, 0.61538462, 0.73201949,
                                          0.70119697, 0.61538462, 0.73235579, 0.70137871, 0.61623932])
  print(model_output)
  model_output = virtualZSS_model.run_model_lstm([0.44651672, 0.40637518, 0.15683761, 0.44736698, 0.40825321,
                                          0.15854701, 0.44787555, 0.4098277, 0.16068376, 0.44836012,
                                          0.41188712, 0.16239316, 0.4490382, 0.40774749, 0.16111111,
                                          0.44979481, 0.40907849, 0.15940171, 0.45049222, 0.40958,
                                          0.15940171, 0.45107263, 0.41246612, 0.16111111, 0.45162922,
                                          0.41216323, 0.15940171, 0.45237498, 0.4136065, 0.15769231,
                                          0.45252389, 0.41552644, 0.15555556, 0.45314099, 0.415446,
                                          0.15555556, 0.45357328, 0.41491479, 0.15512821, 0.45441989,
                                          0.41413176, 0.15555556, 0.45447624, 0.41444948, 0.15598291,
                                          0.45490745, 0.41439553, 0.15598291, 0.45533412, 0.41200947,
                                          0.15598291, 0.45701545, 0.41350456, 0.15598291, 0.45716559,
                                          0.41274214, 0.15598291, 0.45799572, 0.41521592, 0.15811966])
  print(model_output)
'''model_output = virtualZSS_model.run_model(.3, 0.0, .3, .5)
print(model_output)
model_output = virtualZSS_model.run_model(.05, .3, .4, .6)
print(model_output)
model_output = virtualZSS_model.run_model(.7, .85, .55, .5)
print(model_output)'''
