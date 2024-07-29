from unidecode import unidecode
import pandas as pd
import plotly.express as px

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

def scrapp():
    df = pd.read_excel("C:\\Users\\Rat Code\Desktop\\project_dashboard\\workers\\quadro_geral.xlsx")
    return df

def clean_columns(df):
   df.columns = (df.columns.str.strip().str.replace(' ', '_').str.lower()).map(unidecode)
   return df

def percents(df,x):
    counts = df[x].value_counts().reset_index()
    counts.columns = [x,'contagem']
    counts['porcentagem'] = (counts['contagem'] / counts['contagem'].sum()) * 100
    return counts

def percents_men(df,x):
    df = df[df['sexo'] == 'M' ]
    counts = df[x].value_counts().reset_index()
    counts.columns = [x,'contagem']
    counts['porcentagem'] = (counts['contagem'] / counts['contagem'].sum()) * 100
    return counts

def percents_women(df,x):
    df = df[df['sexo'] == 'F' ]
    counts = df[x].value_counts().reset_index()
    counts.columns = [x,'contagem']
    counts['porcentagem'] = (counts['contagem'] / counts['contagem'].sum()) * 100
    return counts

def manager(x):
    df = clean_columns(scrapp())
    calc_percents = percents(df,x)
    return calc_percents

def manager_men(x):
    df = clean_columns(scrapp())
    calc_percents = percents_men(df,x)
    return calc_percents

def manager_womens(x):
    df = clean_columns(scrapp())
    calc_percents = percents_women(df,x)
    return calc_percents


#criando graficos
def bar_graph():
    graph = manager('grau_hierarquico')
    fig_hierarchy = px.bar(graph, x='grau_hierarquico', y='contagem', text='porcentagem', title="Grau Hierárquico")
    graph = manager('posto')
    fig_post = px.bar(graph, x='posto', y='contagem', text='porcentagem', title="Posto")
    graph = manager('escala')
    fig_shift = px.bar(graph, x='escala', y='contagem', text='porcentagem', title="Escala")
    graph = manager('afastamento')
    fig_afast = px.bar(graph, x='afastamento', y='contagem',title='Afastamento')
    return fig_hierarchy,fig_post,fig_shift,fig_afast

def pie_graph():
    graph = manager('companhia')
    fig_company = px.pie(graph, names='companhia', values='contagem', title="Companhia")
    graph = manager('sexo')
    fig_gender = px.pie(graph, names='sexo', values='contagem', title="Sexo", hole=0.1)
    graph = manager('situacao_sanitaria')
    fig_sanitary = px.pie(graph, names='situacao_sanitaria', values='contagem',title='Situação Sanitária')
    return fig_company,fig_gender,fig_sanitary

def dispersion():
    graph = manager('ala')
    fig_ala = px.scatter(graph,x='ala',y='contagem',title='Alas',labels={'ala':'Nome da Ala','contagem':'Porcentagem de Militares'})
    return fig_ala
    
#criando graficos só homens
def bar_graph_mens():
    graph = manager_men('grau_hierarquico')
    fig_hierarchy = px.bar(graph, x='grau_hierarquico', y='contagem', text='porcentagem', title="Grau Hierárquico")
    graph = manager('posto')
    fig_post = px.bar(graph, x='posto', y='contagem', text='porcentagem', title="Posto")
    graph = manager_men('escala')
    fig_shift = px.bar(graph, x='escala', y='contagem', text='porcentagem', title="Escala")
    graph = manager_men('afastamento')
    fig_afast = px.bar(graph, x='afastamento', y='contagem',title='Afastamento')
    return fig_hierarchy,fig_post,fig_shift,fig_afast

def pie_graph_mens():
    graph = manager_men('companhia')
    fig_company = px.pie(graph, names='companhia', values='contagem', title="Companhia")
    graph = manager_men('sexo')
    fig_gender = px.pie(graph, names='sexo', values='contagem', title="Sexo", hole=0.1)
    graph = manager_men('situacao_sanitaria')
    fig_sanitary = px.pie(graph, names='situacao_sanitaria', values='contagem',title='Situação Sanitária')
    return fig_company,fig_gender,fig_sanitary

def dispersion_mens():
    graph = manager_men('ala')
    fig_ala = px.scatter(graph,x='ala',y='contagem',title='Alas',labels={'ala':'Nome da Ala','contagem':'Porcentagem de Militares'})
    return fig_ala
    
#criando graficos só Mulheres
def bar_graph_womens():
    graph = manager_womens('grau_hierarquico')
    fig_hierarchy = px.bar(graph, x='grau_hierarquico', y='contagem', text='porcentagem', title="Grau Hierárquico")
    graph = manager('posto')
    fig_post = px.bar(graph, x='posto', y='contagem', text='porcentagem', title="Posto")
    graph = manager_womens('escala')
    fig_shift = px.bar(graph, x='escala', y='contagem', text='porcentagem', title="Escala")
    graph = manager_womens('afastamento')
    fig_afast = px.bar(graph, x='afastamento', y='contagem',title='Afastamento')
    return fig_hierarchy,fig_post,fig_shift,fig_afast

def pie_graph_womens():
    graph = manager_womens('companhia')
    fig_company = px.pie(graph, names='companhia', values='contagem', title="Companhia")
    graph = manager_womens('sexo')
    fig_gender = px.pie(graph, names='sexo', values='contagem', title="Sexo", hole=0.1)
    graph = manager_womens('situacao_sanitaria')
    fig_sanitary = px.pie(graph, names='situacao_sanitaria', values='contagem',title='Situação Sanitária')
    return fig_company,fig_gender,fig_sanitary

def dispersion_womens():
    graph = manager_womens('ala')
    fig_ala = px.scatter(graph,x='ala',y='contagem',title='Alas',labels={'ala':'Nome da Ala','contagem':'Porcentagem de Militares'})
    return fig_ala