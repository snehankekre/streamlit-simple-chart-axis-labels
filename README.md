# streamlit-simple-chart-axis-labels

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://simple-chart-axis-labels-demo.streamlit.app)

Streamlit's [simple charts](https://docs.streamlit.io/develop/api-reference/charts#simple-chart-elements) (line, area, bar, scatter) have `x_title` and `y_title` parameters that allow you to customize the axis titles.

| Parameter | Description |
| --- | --- |
| `x_title` *(str, or None)* | The title of the x-axis. If None, either the column name specified in ``x`` will be used, or no title will be displayed. |
| `y_title` *(str, or None)* | The title of the y-axis. If None, either the column name specified in ``y`` will be used, or no title will be displayed. |

See the [PoC implementation](https://github.com/streamlit/streamlit/compare/develop...snehan/feature/chart-titles)
