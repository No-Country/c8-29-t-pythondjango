import requests
import pandas as pd



def send_jobs_csv(file):
    df = pd.read_csv(f"{file}")
    for i in df.index:
        title = df['title'][i]
        subtitle = df['subtitle'][i]
        sub_subtitle = df['sub_subtitle'][i]
        company = df['company'][i]
        salary = df['salary'][i]
        description = df['description'][i]
        date_publish = df['date_publish'][i]
        url_postulacion = df['url_postulacion'][i]
        type_job = df['type'][i]
        location = df['location'][i]


        parameters = {"title":title,
                      "subtitulo":subtitle,
                      "sub_subtitulo":sub_subtitle,
                      "company":company,
                      "salary":salary,
                      "description":description,
                      "date_publish":date_publish,
                      "url_postulation":url_postulacion,
                      "location":location,
                      "type":type_job}
        response = requests.post("http://127.0.0.1:8000/add-job", json=parameters)
        print(response.status_code)

def send_jobs(title, sub_subtitle, description, date_publish, subtitle, url_postulacion, company_type, company, salary, location,):
        print("enviando trabajo")
        parameters = {"title":title,
                      "subtitulo":subtitle,
                      "sub_subtitulo":sub_subtitle,
                      "company":company,
                      "salary":salary,
                      "description":description,
                      "date_publish":str(date_publish),
                      "url_postulation":url_postulacion,
                      "location":location,
                      "type":company_type}
        print(parameters)
        response = requests.post("http://54.166.3.214:8000/add-job", json=parameters)
        print(response.status_code)


