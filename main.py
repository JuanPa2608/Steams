from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/inicio")
async def ruta_prueba():
    return "Hola"

df_PlayTimeGenre = pd.read_parquet('Funciones/datasets/PlayTimeGenre.parquet')

@app.get("/PlayTimeGenre")
async def PlayTimeGenre(genre):
    anio = df_PlayTimeGenre['release_year'][df_PlayTimeGenre['Sum_playtime_forever'][df_PlayTimeGenre['genres'] == genre].idxmax()]
    return str('Año de lanzamiento con más horas jugadas para Género ' + genre + ': ' + str(anio))

df_UserForGenre = pd.read_parquet('Funciones/datasets/UserForGenre_total.parquet')

@app.get("/UserForGenre")
async def UserForGenre(genre):
    user = df_UserForGenre[genre][0]
    lista = df_UserForGenre[genre][1]
    return str('Usuario con más horas jugadas para Género ' + genre + ': ' + user + ' Horas jugadas: ' + lista)

df_UsersRecommend = pd.read_parquet('Funciones/datasets/UsersRecommend.parquet')

@app.get("/UsersRecommend")
async def UsersRecommend(anio):
    top_recomend = df_UsersRecommend[df_UsersRecommend['year_posted'] == int(anio)]
    top_recomend.reset_index(drop = True,inplace = True)
    return str('Items_id-Item_Name Puesto 1: '+ top_recomend['item_id'][0] + '-' + top_recomend['item_name'][0] +
                ' Puesto 2: '+ top_recomend['item_id'][1] + '-' + top_recomend['item_name'][1] +
                ' Puesto 3: '+ top_recomend['item_id'][2] + '-' + top_recomend['item_name'][2] )
    
df_UsersNotRecommend = pd.read_parquet('Funciones/datasets/UsersNotRecommend.parquet')

@app.get("/UsersNotRecommend")
async def UsersNotRecommend(anio):
    top_not_recomend = df_UsersNotRecommend[df_UsersNotRecommend['year_posted'] == int(anio)]
    top_not_recomend.reset_index(drop = True,inplace = True)
    return str('Items_id-Item_Name Puesto 1: '+ top_not_recomend['item_id'][0] + '-' + top_not_recomend['item_name'][0] +
                ' Puesto 2: '+ top_not_recomend['item_id'][1] + '-' + top_not_recomend['item_name'][1] +
                ' Puesto 3: '+ top_not_recomend['item_id'][2] + '-' + top_not_recomend['item_name'][2] )
    
df_SentimentRecommend = pd.read_parquet('Funciones/datasets/SentimentRecommend.parquet')

@app.get("/sentiment_analysis")
async def sentiment_analysis(anio):
    analisis_sentimiento = df_SentimentRecommend[df_SentimentRecommend['year_posted'] == int(anio)]
    return str('Negative: '+ str(analisis_sentimiento['sentiment_analysis'][analisis_sentimiento['sentiment_analysis'] == 'Negative'].count()) +
                 ' Neutral: '+ str(analisis_sentimiento['sentiment_analysis'][analisis_sentimiento['sentiment_analysis'] == 'Neutral'].count()) +
                 ' Positive: '+ str(analisis_sentimiento['sentiment_analysis'][analisis_sentimiento['sentiment_analysis'] == 'Positive'].count()))

