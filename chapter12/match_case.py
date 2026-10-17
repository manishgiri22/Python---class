def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "page not found"
        case 500:
            return "internal server error"
        case __:
            return"unknown error"
print(http_status(404))
