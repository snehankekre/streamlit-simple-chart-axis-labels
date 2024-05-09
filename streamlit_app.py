import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Simple Chart Axis Titles",
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


st.subheader("Customizing Axis Titles for Streamlit's Simple Charts")

with st.expander("Context :books:"):
    st.write(
        """
    Streamlit's [simple charts](https://docs.streamlit.io/develop/api-reference/charts#simple-chart-elements) (line, area, bar, scatter) have `x_title` and `y_title` parameters that allow you to customize the axis titles.

    | Parameter | Description |
    | --- | --- |
    | `x_title` *(str, or None)* | The title of the x-axis. If None, either the column name specified in ``x`` will be used, or no title will be displayed. |
    | `y_title` *(str, or None)* | The title of the y-axis. If None, either the column name specified in ``y`` will be used, or no title will be displayed. |


    """
    )

    st.write(
        """


    """
    )

    st.write(
        """
    - Notion project: [Built-in charts: Customizable axis titles](https://www.notion.so/snowflake-corp/Product-spec-202a693205e046e28c451bc43d18f11c)
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
#     x_title="This is the x-axis title",
# )


chart_data = load_data()

x_title = st.text_input(label="Enter the x-axis title", value="This is the x-axis title", help="This is the x-axis title that will be displayed below the x-axis.")
y_title = st.text_input(label="Enter the y-axis title", value="This is the y-axis title", help="This is the y-axis title that will be displayed to the left of the y-axis.")

tab1, tab2, tab3, tab4 = st.tabs(["Line Chart", "Area Chart", "Bar Chart", "Scatter Chart"])

with tab1:
    st.line_chart(
        chart_data,
        x="a",
        y="b",
        use_container_width=True,
        x_title=x_title,
        y_title=y_title,
    )
    st.code(
    f"""
    st.line_chart(
        chart_data,
        x="a",
        y="b",
        use_container_width=True,
        x_title="{x_title}",
        y_title="{y_title}",
    )
    """
    )

with tab2:
    st.area_chart(
        chart_data,
        use_container_width=True,
        x_title=x_title,
        y_title=y_title,
    )
    st.code(
    f"""
    st.area_chart(
        chart_data,
        use_container_width=True,
        x_title="{x_title}",
        y_title="{y_title}",
    )
    """
    )

with tab3:
    st.bar_chart(
        chart_data,
        use_container_width=True,
        x_title=x_title,
        y_title=y_title,
    )

    st.code(
    f"""
    st.bar_chart(
        chart_data,
        use_container_width=True,
        x_title="{x_title}",
        y_title="{y_title}",
    )
    """
    )
with tab4:
    st.scatter_chart(
        chart_data,
        use_container_width=True,
        x_title=x_title,
        y_title=y_title,
    )
    st.code(
    f"""
    st.scatter_chart(
        chart_data,
        use_container_width=True,
        x_title="{x_title}",
        y_title="{y_title}",
    )
    """
    )



