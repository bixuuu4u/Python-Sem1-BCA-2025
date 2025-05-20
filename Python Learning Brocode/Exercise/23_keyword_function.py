def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=91,area=759,first=865,last=4584)
print(phone_num)