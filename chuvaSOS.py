from data.cityCode import cityCode
from os.path import exists
from ydata_profiling import ProfileReport
from data.raw_data import getting_data
from data.processed_data import process_data


unprocessed_data = getting_data(cityCode.Barra_de_Guabiraba.value)

dataframe = process_data(unprocessed_data)


profile = ProfileReport(df=dataframe, title='TEST')
file_existis = exists('chuvaSOS.html')

if file_existis != True:
    profile.to_file('ChuvaSOS.html')
