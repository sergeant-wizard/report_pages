import pandas


pandas.DataFrame({
    'a': [0, 1, 2],
    'b': [10, 11, 12],
}, index=['s1', 's2', 's3']).to_html('docs/_includes/table.html')
