import streamlit as st
import pandas as pd
import numpy as np

# Generate some sample data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Display line chart
st.line_chart(data)
