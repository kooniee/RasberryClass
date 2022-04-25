def Domain_name(string):
    URL = "http://github.com/carbonfive/raygun"

    domain = URL.replace("http://", " ")
    domain1 = domain[:domain.index(".")]  
    print("{0}".format(domain1))
Domain_name("http://github.com/carbonfive/raygun")

