def domain_name(url):
    replace_values = {"https://": "", "http://": "", "www.": ""}
    for i, j in replace_values.items():  # clear protocol and sub-domain
        url = url.replace(i, j)
    return url.split('.')[0]


# test

assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
