from django.shortcuts import render, redirect
from emailforms.forms import EmailForm
import requests
from requests.auth import HTTPBasicAuth
import json


def home(request):
    return render(request=request, template_name="portfolio/landing.html")


def about(request):
    return render(request=request, template_name="portfolio/about.html")


def projects(request):
    url = "https://fnbb.atlassian.net/rest/api/3/project/search"
    auth = HTTPBasicAuth("nolanpgregory@gmail.com",
                         "ATATT3xFfGF0zq5deuFVo0VGgVlUkChM2v6S_dqJGgOH1PnYCrgASxX6odCpg9gALXk-CDj_XezJJE8M7g-jCzTwTAvVe6cRYoz_GQL3y7pKuYh1XLw9LGcEQWGSi71mfjBnDw2hF-BX0i2LvaHIeO77dpNs1BrQW8q1mbtXo_uHCcq90nfN_JY=8BE4C8D8")
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    jira_projects = json.loads(response.text)["values"]
    names = []
    data = []
    for i in jira_projects:
        for j in i:
            if j == "key":
                names.append(i[j])

    for k in names:
        url = f"https://fnbb.atlassian.net/rest/api/3/project/{k}"

        headers = {
            "Accept": "application/json"
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        )
        data.append(json.loads(response.text))

    url = "https://fnbb.atlassian.net/rest/api/2/search?jql=ORDER%20BY%20Created"
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )

    issues = json.loads(response.text)["issues"]

    context = {"data": data,
               "issues": issues}

    return render(context=context, request=request, template_name="portfolio/projects.html")


def blog(request):
    return render(request=request, template_name="portfolio/blog.html")


def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('main')
    else:
        form = EmailForm()
    return render(request, 'portfolio/contact.html', {'form': form})
