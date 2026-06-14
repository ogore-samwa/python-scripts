def print_sample_invitation(mother, father, child, teacher, event):
    sample_text = f'''
Dear {mother} and {father}.
{teacher} and I would love to see you both as well as {child} at our {event} tomorrow morning.

Best regards,
Principal G. Stanley.
'''
    print(sample_text)
print_sample_invitation(mother='Noel', father='Ogore', child='J.J', teacher='Joshua', event='Graduation')
