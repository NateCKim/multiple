# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
v5m_Sales_Records = dataiku.Dataset("5m_Sales_Records")
v5m_Sales_Records_df = v5m_Sales_Records.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

v5mil_df = v5m_Sales_Records_df # For this sample code, simply copy input to output


# Write recipe outputs
v5mil = dataiku.Dataset("5mil")
v5mil.write_with_schema(v5mil_df)
