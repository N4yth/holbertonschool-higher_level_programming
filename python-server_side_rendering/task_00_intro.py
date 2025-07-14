
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        return "template must be a string"
    if not isinstance(attendees, list):
        return "attendees must be a list"
    if template == "":
        return "Template is empty, no output files generated."
    if attendees == []:
        return "No data provided, no output files generated."

    for i, element in enumerate(attendees):
        result = template
        for index, value in element.items():
            print(index)
            if (element.get("{}".format(index))):
                result = result.replace("{"+"{}".format(index)+"}", value)
            else:
                result = result.replace("{"+"{}".format(index)+"}", "N/A")
        with open("output_{}.txt".format(i + 1),
                  'w', encoding='UTF-8') as fichier:
            fichier.write(result)
