
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        return "template must be a string"
    if not isinstance(attendees, list):
        return "attendees must be a list"
    if template == "":
        return "Template is empty, no output files generated."
    if attendees == []:
        return "No data provided, no output files generated."

    key_list = ["name", "event_title", "event_date", "event_location"]

    for i, element in enumerate(attendees):
        result = template
        for key in key_list:
            value = element.get(key)
            if (value is None):
                value = "N/A"
            result = result.replace("{"+"{}".format(key)+"}", value)
        with open("output_{}.txt".format(i + 1),
                  'w', encoding='UTF-8') as fichier:
            fichier.write(result)
