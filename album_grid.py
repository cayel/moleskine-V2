def generate_css(color):
    return f"""
    <style>
    .album-info {{
        font-size: 10px;
        line-height: 1.2;
        margin-top: 0;
        color: white;
    }}
    .album-table {{
        width: 100%;
        border-collapse: collapse;
        border: 1px solid {color}; 
        background-color: {color}; 
    }}
    .album-table td {{
        padding: 2px;
        border: none;
    }}
    .album-table tr {{
        padding: 2px;
        border: none;
    }}
    .album-table img {{
        width: 100%;
    }}
    </style>
    """

def generate_table_html(list_releases, num_columns):
    table_html = '<table class="album-table">'
    column_count = 0

    for release in list_releases.releases:
        if column_count == 0:
            table_html += '<tr>'
        table_html += f"<td rowspan='1'><img src='{release.image}' title='{release.title}' style='width:150px; height:auto;'></td>"
        column_count += 1
        if column_count == num_columns:
            table_html += '</tr>'
            column_count = 0

    if column_count != 0:
        table_html += '</tr>'

    table_html += '</table>'
    return table_html

def generate_table_html_array(releases, num_columns):
    table_html = '<table class="album-table">'
    column_count = 0

    for release in releases:
        if column_count == 0:
            table_html += '<tr>'
        search_query = release.title.replace(' ', '%20')
        spotify_search_url = f"https://open.spotify.com/search/{search_query}"
        table_html += f"<td rowspan='1'><a href='{spotify_search_url}' target='_blank'><img src='{release.image}' title='{release.title}' style='width:150px; height:auto;'></a></td>"
        column_count += 1
        if column_count == num_columns:
            table_html += '</tr>'
            column_count = 0

    if column_count != 0:
        table_html += '</tr>'

    table_html += '</table>'
    return table_html