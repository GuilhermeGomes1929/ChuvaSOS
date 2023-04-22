def get_tag_content(tag):
    return tag.text

def concat_date_and_time(date_list):
    date_list_concat = []
    for i in range(len(date_list)):
        if i % 2 == 1:
            date_list_concat.append(
                str(date_list[i].text) + ' ' + str(date_list[i - 1].text))
    return date_list_concat