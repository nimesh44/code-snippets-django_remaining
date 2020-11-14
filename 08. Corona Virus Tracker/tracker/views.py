from django.shortcuts import render
import requests
import csv

# Create your views here.

def home(request):
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    # For large data set stream to true
    # Response is stored in r variable
    r = requests.get(url,stream = True)
    # print(r.iter_lines())
    f =  (line.decode('utf-8') for line in r.iter_lines())
    # print(f)
    # Getting csv file as list
    reader = list(csv.reader(f))
    # print(reader)
    # Getting first index which is first row
    # print(reader[0])

    # For worldwide data
    word_covid_list = []
    today_total_cases = 0
    yesterday_total_cases = 0
    day_before_yesterday = 0
    for row in reader[1:]:
        temp ={
            'country':row[1],
            'province': row[0],
            'posetive_cases': row[-1]
        }
        word_covid_list.append(temp)
        today_total_cases += int(row[-1])
        yesterday_total_cases += int(row[-2])
        day_before_yesterday += int(row[-3])
    posetive_added_today = today_total_cases - yesterday_total_cases
    posetive_added_yesterday = yesterday_total_cases - day_before_yesterday
    # How our new list look like
    print(word_covid_list)


    # For nepal only
    nepal_covid_dict = {}
    nepal_today_total_cases = 0
    nepal_yesterday_total_cases = 0
    nepal_day_before_yesterday_total_cases = 0
    for row in reader[1:]:
        if row[1].lower() == 'nepal':
            nepal_today_total_cases += int(row[-1])
            nepal_yesterday_total_cases += int(row[-2])
            nepal_day_before_yesterday_total_cases += int(row[-3])
    nepal_today_added_cases = nepal_today_total_cases - nepal_yesterday_total_cases
    nepal_yesterday_added_cases = nepal_yesterday_total_cases - nepal_day_before_yesterday_total_cases
    # Adding content to dictionary
    nepal_covid_dict['nepal_today_total_cases'] = nepal_today_total_cases
    nepal_covid_dict['nepal_today_added_cases'] = nepal_today_added_cases
    nepal_covid_dict['nepal_yesterday_added_cases'] = nepal_yesterday_added_cases
    print(nepal_covid_dict)

    # passing data to template as context
    context ={
        'covid_info': word_covid_list,
        'today_total_cases': today_total_cases,
        'yesterday_total_cases': yesterday_total_cases,
        'posetive_added_today': posetive_added_today,
        'posetive_added_yesterday': posetive_added_yesterday,
        'nepal': nepal_covid_dict,
        'nepal_today_total_cases': nepal_today_total_cases,
        'nepal_today_added_cases': nepal_today_added_cases,
        'nepal_yesterday_added_cases': nepal_yesterday_added_cases,
    }

    return render(request,'tracker/home.html',context)
