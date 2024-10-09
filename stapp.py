import streamlit as st
import pandas as pd
import matplotlib as plt
st.title ("Sample Streamlit App")
df = pd.read_csv("DataCoSupplyChainDataset.csv", encoding="unicode_escape", nrows=1000)

# st.dataframe(df)
# describe the dataframe

st.write("### Data Preview ")
#add a link to click
url='https://github.com/ashishpatel26/DataCo-SMART-SUPPLY-CHAIN-FOR-BIG-DATA-ANALYSIS'
st.markdown("Public Data taken from this [link](%s)" % url)

st.write(df.head())
st.markdown("### Data Stats")

st.write(df.describe())

# pd.set_option('display.max_columns', None)

#plot "Order Item Total" by "Order Date"

# st.write(df.columns)
# df.plot(x="order date (DateOrders)", y="Order Item Total", kind="bar")
# get mm-yyyy for 'order date (DateOrders)'
df['Order Month'] = pd.to_datetime(df['order date (DateOrders)']).dt.strftime('%Y-%m')
# st.write( (df['order date (DateOrders)']))
#sum Order Item Total by 'order date (DateOrders)'
df_order_by_month = df.groupby('Order Month').sum()['Order Item Total'].reset_index()
# st.write(df_order_by_month)
st.markdown('### Plot')
st.bar_chart(data=df_order_by_month,x="Order Month",y="Order Item Total")
# st.bar_chart(df_order_by_month)
#chart data should be date in month-year format and order item total
# chart_Data should be df['order date (DateOrders)']  and Order item total
# chart_data = pd.DataFrame(df, columns=['order date (DateOrders)', 'Order Item Total'])


# chart_data = df.groupby('order date (DateOrders)').sum()['Order Item Total'].reset_index()
# chart_data = pd.DataFrame(df, columns=['order date (DateOrders)', 'Order Item Total'])
# st.bar_chart(chart_data)