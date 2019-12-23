import pandas

import my_module.hoge


pandas.DataFrame(
    my_module.hoge.get_results(),
    index=['s1', 's2', 's3']
).to_html('docs/_includes/table.html')
