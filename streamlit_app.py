import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Simple Chart Axis Labels",
    page_icon=":bar_chart:",
)


@st.cache_data
def load_col_data():
    return pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )


@st.cache_data
def load_data():
    return pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


st.subheader("Customizing Axis Labels for Streamlit's Simple Charts")

with st.expander("Context :books:"):
    st.write(
        """
    Streamlit's [simple charts](https://docs.streamlit.io/develop/api-reference/charts#simple-chart-elements) (line, area, bar, scatter) have a `title_x` and `title_y` parameters that allow you to customize the axis labels.

    | Parameter | Description |
    | --- | --- |
    | `title_x` *(str, or None)* | The title of the x-axis. If None, either the column name specified in ``x`` will be used, or no title will be displayed. |
    | `title_y` *(str, or None)* | The title of the y-axis. If None, either the column name specified in ``y`` will be used, or no title will be displayed. |


    """
    )

    st.write(
        """


    """
    )

    st.write(
        """
    - Notion project: [Built-in charts: Customizable axis labels](https://www.notion.so/snowflake-corp/Product-spec-202a693205e046e28c451bc43d18f11c)
    - Download the [wheel file](https://github.com/snehankekre/streamlit-simple-chart-axis-labels/raw/main/streamlit-1.33.0-py2.py3-none-any.whl)
    - See the PoC implementation: https://github.com/streamlit/streamlit/compare/develop...snehan/feature/chart-titles
    """
    )

# chart_data = load_col_data()

# st.area_chart(
#     chart_data,
#     x="col1",
#     y="col2",
#     color="col3",
#     use_container_width=True,
#     title_x="This is the x-axis title",
# )


chart_data = load_data()

tab1, tab2, tab3, tab4 = st.tabs(["Line Chart", "Area Chart", "Bar Chart", "Scatter Chart"])

with tab1:
    with st.echo(code_location="below"):
        st.line_chart(
            chart_data,
            x="a",
            y="b",
            use_container_width=True,
            title_x="This is the x-axis title",
            title_y="This is the y-axis title",
        )

with tab2:
    with st.echo(code_location="below"):
        st.area_chart(
            chart_data,
            use_container_width=True,
            title_x="This is the x-axis title",
            title_y="This is the y-axis title",
        )

with tab3:
    with st.echo(code_location="below"):
        st.bar_chart(
            chart_data,
            use_container_width=True,
            title_x="This is the x-axis title",
            title_y="This is the y-axis title",
        )

with tab4:
    with st.echo(code_location="below"):
        st.scatter_chart(
            chart_data,
            use_container_width=True,
            title_x="This is the x-axis title",
            title_y="This is the y-axis title",
        )




