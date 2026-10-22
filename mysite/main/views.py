from django.shortcuts import render


def home(request):
    links = [
        {"title": "Home", "url": "http://127.0.0.1:8000/"},
        {"title": "about", "url": "http://127.0.0.1:8000/about"},
        {"title": "contact", "url": "http://127.0.0.1:8000/contact"}
    ]

    context = {"link": links}

    return render(request, "main/home.html", context)


def about(request):
    info = {
        "name": "Iskender",
        "age": 14,
        "want": ["awqat", "uyqi"],
    }
    return render(request, "main/about.html", info)


def contact(request):
    if request.method == "POST":
        input_name = request.POST.get("user_name")

        return render(request, "main/contact.html", {
            "submited_name": input_name
        })

    return render(request, "main/contact.html")

