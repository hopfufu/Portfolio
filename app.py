from hashlib import new
from optparse import Option
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import pydeck as pdk 
from plotly.offline import init_notebook_mode,iplot,plot
init_notebook_mode(connected=True)



# ol_dict=pickle.load(open('olympic.pkl','rb'))
# olympic_df=pd.DataFrame(ol_dict)



df=pd.read_csv('olympics_medals_country_wise.csv')
st.title('Complete Olympics statistics since 1982')


st.write('No of Gold Medals won by each Country at Summer Olympics')
hideMap="""
    <style>
    .plot-container plotly{
        visibility:hidden;
    }   
"""




if st.button('Gold medal stats'):
    data2=dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        locations = df['countries '],
        locationmode = "country names",
        z = df['summer_gold'],
        text = df['countries '],
        colorbar = {'title' : 'Olympics'},
    )
    layout1 = dict(title = '',
                geo = dict(projection = {'type':'mercator'})
                )
    st.markdown(hideMap,unsafe_allow_html=True)
    choromap = go.Figure(data = [data2],layout = layout1)
    st.plotly_chart(choromap)
st.write('No of Silver Medals won by each Country at Summer Olympics')
if st.button('Silver Medal stats'):
    data2=dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        locations = df['countries '],
        locationmode = "country names",
        z = df['summer_silver'],
        text = df['countries '],
        colorbar = {'title' : 'Olympics'},
    )
    layout1 = dict(title = '',
                geo = dict(projection = {'type':'mercator'})
                )
    choromap = go.Figure(data = [data2],layout = layout1)
    st.plotly_chart(choromap)
st.write('No of Bronze Medals won by each Country at Summer Olympics')
if st.button('Bronze Medal stats'):
    data2=dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        locations = df['countries '],
        locationmode = "country names",
        z = df['summer_bronze'],
        text = df['countries '],
        colorbar = {'title' : 'Olympics'},
    )
    layout1 = dict(title = '',
                geo = dict(projection = {'type':'mercator'})
                )
    choromap = go.Figure(data = [data2],layout = layout1)
    st.plotly_chart(choromap)



#generating a 3d plot for total participation in summer Games
# new_df=df.drop('ioc_code ',axis=1)
# new_df=new_df.drop(df.columns[3:],axis=1)

# st.pydeck_chart(pdk.Deck(
#      map_style=None,
#      initial_view_state=pdk.ViewState(
#          zoom=11,
#          pitch=50,
#      ),
#      layers=[
#          pdk.Layer(
#             'HexagonLayer',
#             data=new_df,
#             get_position=new_df['countries '],
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             pickable=True,
#             extruded=True,
#          ),
#          pdk.Layer(
#              'ScatterplotLayer',
#              data=new_df,
#              get_position=df['summer_participations'],
#              get_color='[200, 30, 0, 160]',
#              get_radius=200,
#          ),
#      ],
#  ))

#generating a line chart
st.write('Summer participants vs goldmedal')
if st.button('Summer vs gold'):
    new_df=pd.DataFrame(df['summer_participations'],df['winter_participations'])
    df2=pd.DataFrame(df['total_gold'],np.arange(152))
    st.line_chart(df2
    )