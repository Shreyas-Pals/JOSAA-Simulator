"""
Bar Chart Page
"""

import streamlit as slt
import altair as alt

remaining_seats = slt.session_state.get('bar_graph_data')
slt.title("Number Of Seats Remaining:")
slt.write(" ")
chart = alt.Chart(remaining_seats).mark_bar(color='#1f77b4').encode(
    x=alt.X('IITs', sort=None),
    y='Seats',
    tooltip=['IITs', 'Seats']
).properties(width=600, height=400)

slt.altair_chart(chart)