from datetime import datetime, timedelta


def get_available_time_slots(hours, appointments, duration=timedelta(hours=1)):
    slots = sorted([(hours[0], hours[0])] + appointments + [(hours[1], hours[1])])
    available_time_slots = []
    for start, end in ((slots[i][1], slots[i + 1][0]) for i in range(len(slots) - 1)):
        assert start <= end, "Cannot attend all appointments"
        while start + duration <= end:
            available_time_slots.append("{:%H:%M} - {:%H:%M}".format(start, start + duration))
            start += duration
    return available_time_slots


def build_appointments_list(appointments):
    appointments_list = []
    for appointment in appointments:
        appointment = (datetime(appointment.time_slot.year,
                                appointment.time_slot.month,
                                appointment.time_slot.day,
                                appointment.time_slot.hour),
                       datetime(appointment.time_slot.year,
                                appointment.time_slot.month,
                                appointment.time_slot.day,
                                appointment.time_slot.hour + 1))

        appointments_list.append(appointment)
    return appointments_list


def get_time_slot(date, time):
    date_list = date.split('-')
    year = date_list[0]
    month = date_list[1]
    day = date_list[2]
    hour = time.split('-')[0].split(':')[0]
    time_slot = datetime(int(year), int(month), int(day), int(hour))
    return time_slot